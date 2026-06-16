from __future__ import annotations

import pytest

from config.settings import TIMEOUT
from fixtures.cart_flow import open_product_detail_and_add_to_cart
from pages.cart_page import CartPage
from pages.home_page import HomePage


def _open_empty_checkout(page, base_url) -> CartPage:
    home = HomePage(page, timeout=TIMEOUT)
    cart = CartPage(page, timeout=TIMEOUT)

    home.open(base_url)
    home.accept_cookie_if_present()
    page.goto(f"{base_url.rstrip('/')}/gio-hang.html", wait_until="domcontentloaded", timeout=TIMEOUT)
    cart.wait_checkout_loaded()
    return cart


def _assert_ward_rejects_special_characters(cart: CartPage, invalid_ward: str) -> None:
    cart.fill_shipping_information(ward=invalid_ward)
    cart.complete_order()
    ward_value = cart.get_ward_value()
    field_is_sanitized = ward_value != invalid_ward and not any(char in ward_value for char in "@#$%")

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with invalid special-character ward value."
    )
    assert field_is_sanitized or cart.has_ward_validation_feedback(), (
        "Expected checkout to block special-character ward by sanitizing the field "
        f"or showing validation feedback, got ward value: {ward_value!r}"
    )


def _assert_phone_rejects_lowercase_letters(cart: CartPage, invalid_phone: str) -> None:
    cart.fill_shipping_information(phone=invalid_phone)
    cart.complete_order()
    phone_value = cart.get_phone_value()
    field_is_sanitized = phone_value != invalid_phone and not any(char.isalpha() for char in phone_value)

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with lowercase letters in phone field."
    )
    assert field_is_sanitized or cart.has_phone_validation_feedback(), (
        "Expected checkout to block lowercase letters in phone by sanitizing the field "
        f"or showing validation feedback, got phone value: {phone_value!r}"
    )


def _assert_name_rejects_special_characters(cart: CartPage, invalid_name: str) -> None:
    cart.fill_shipping_information(name=invalid_name)
    cart.complete_order()
    name_value = cart.get_name_value()
    field_is_sanitized = name_value != invalid_name and not any(char in name_value for char in "@#$%")

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with special characters in customer name."
    )
    assert field_is_sanitized or cart.has_name_validation_feedback(), (
        "Expected checkout to block special characters in customer name by sanitizing the field "
        f"or showing validation feedback, got name value: {name_value!r}"
    )


def _assert_name_rejects_digits(cart: CartPage, invalid_name: str) -> None:
    cart.fill_shipping_information(name=invalid_name)
    cart.complete_order()
    name_value = cart.get_name_value()
    field_is_sanitized = name_value != invalid_name and not any(char.isdigit() for char in name_value)

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with digits in customer name."
    )
    assert field_is_sanitized or cart.has_name_validation_feedback(), (
        "Expected checkout to block digits in customer name by sanitizing the field "
        f"or showing validation feedback, got name value: {name_value!r}"
    )


def _assert_address_rejects_blank_value(cart: CartPage, invalid_address: str) -> None:
    cart.fill_shipping_information(address=invalid_address)
    cart.complete_order()
    address_value = cart.get_address_value()
    field_is_sanitized = not address_value

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with blank shipping address."
    )
    assert field_is_sanitized or cart.has_address_validation_feedback(), (
        "Expected checkout to block whitespace-only shipping address by treating it as blank "
        f"or showing validation feedback, got address value: {address_value!r}"
    )


def _assert_address_rejects_special_characters(cart: CartPage, invalid_address: str) -> None:
    cart.fill_shipping_information(address=invalid_address)
    cart.complete_order()
    address_value = cart.get_address_value()
    field_is_sanitized = address_value != invalid_address and not any(char in address_value for char in "@#$%")

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order with special characters in shipping address."
    )
    assert field_is_sanitized or cart.has_address_validation_feedback(), (
        "Expected checkout to block special characters in shipping address by sanitizing the field "
        f"or showing validation feedback, got address value: {address_value!r}"
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_submit_without_product_is_handled_gracefully(page, base_url, test_data):
    cart = _open_empty_checkout(page, base_url)

    cart.fill_shipping_information(ward=test_data["checkout"]["valid_ward"])
    cart.complete_order()

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete an order when cart has no product."
    )
    assert cart.has_empty_checkout_validation_feedback(), (
        "Expected checkout to show a clear validation message when submitting without product."
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_ward_field_rejects_special_characters_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_ward_rejects_special_characters(
        cart,
        test_data["checkout"]["invalid_special_character_ward"],
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_phone_field_rejects_lowercase_letters_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_phone_rejects_lowercase_letters(
        cart,
        test_data["checkout"]["invalid_lowercase_phone"],
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_name_field_accepts_lowercase_letters_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    lowercase_name = test_data["checkout"]["lowercase_name"]
    cart.fill_shipping_information(
        name=lowercase_name,
        phone=test_data["checkout"]["invalid_lowercase_phone"],
    )
    cart.complete_order()

    assert not cart.is_order_success_visible(), (
        "Expected checkout not to complete while using an invalid phone guard value."
    )
    assert cart.get_name_value() == lowercase_name, (
        "Expected customer name field to allow lowercase letters after submit is blocked."
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_name_field_rejects_special_characters_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_name_rejects_special_characters(
        cart,
        test_data["checkout"]["invalid_special_character_name"],
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_name_field_rejects_digits_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_name_rejects_digits(
        cart,
        test_data["checkout"]["invalid_numeric_name"],
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_address_field_rejects_blank_value_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_address_rejects_blank_value(
        cart,
        test_data["checkout"]["invalid_blank_address"],
    )


@pytest.mark.cart
@pytest.mark.edge
def test_checkout_address_field_rejects_special_characters_with_product(page, base_url, test_data):
    cart, _ = open_product_detail_and_add_to_cart(page, base_url, test_data)
    cart.wait_cart_rendered()

    assert cart.has_cart_content(), "Expected cart to contain product before checkout validation."
    _assert_address_rejects_special_characters(
        cart,
        test_data["checkout"]["invalid_special_character_address"],
    )
