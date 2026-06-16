from __future__ import annotations


GROUP_ORDER = ("cart", "navigation", "product", "search", "ui")
GROUP_INDEX = {group: index for index, group in enumerate(GROUP_ORDER)}


TEST_CASE_DEFINITIONS = [
    # Cart / checkout
    {
        "path": "tests/cart/test_cart_suite.py",
        "function": "test_cart_quantity_update",
        "title": "Update cart quantity",
        "purpose": "Verify plus and minus controls keep cart quantity in a valid non-decreasing/non-increasing state.",
    },
    {
        "path": "tests/cart/test_cart_suite.py",
        "function": "test_cart_persistence",
        "title": "Cart persists after reload",
        "purpose": "Verify cart content remains visible after reloading the cart or checkout page.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_submit_without_product_is_handled_gracefully",
        "title": "Checkout submit without product is handled gracefully",
        "purpose": "Verify checkout does not hang, navigate incorrectly, or complete an order when submitting shipping information with an empty cart.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_ward_field_rejects_special_characters_with_product",
        "title": "Checkout ward field rejects special characters with product",
        "purpose": "Verify ward field does not keep a value made only from special characters when checkout has a product.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_phone_field_rejects_lowercase_letters_with_product",
        "title": "Checkout phone field rejects lowercase letters with product",
        "purpose": "Verify phone field does not keep lowercase letters when checkout has a product.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_name_field_accepts_lowercase_letters_with_product",
        "title": "Checkout name field accepts lowercase letters with product",
        "purpose": "Verify customer name field keeps lowercase letters after checkout submit is blocked by another invalid field.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_name_field_rejects_special_characters_with_product",
        "title": "Checkout name field rejects special characters with product",
        "purpose": "Verify customer name field does not keep a value made only from special characters when checkout has a product.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_name_field_rejects_digits_with_product",
        "title": "Checkout name field rejects digits with product",
        "purpose": "Verify customer name field does not keep a value made only from digits when checkout has a product.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_address_field_rejects_blank_value_with_product",
        "title": "Checkout address field rejects blank value with product",
        "purpose": "Verify shipping address field treats a whitespace-only value as blank and does not complete checkout.",
    },
    {
        "path": "tests/cart/test_checkout_validation_suite.py",
        "function": "test_checkout_address_field_rejects_special_characters_with_product",
        "title": "Checkout address field rejects special characters with product",
        "purpose": "Verify shipping address field does not keep a value made only from special characters when checkout has a product.",
    },
    # Navigation
    {
        "path": "tests/navigation/test_navigation_additional_suite.py",
        "function": "test_home_page_returns_success_and_non_blank_content",
        "title": "Home page loads successfully",
        "purpose": "Verify the home page returns no server error and renders non-blank content.",
    },
    {
        "path": "tests/navigation/test_navigation_additional_suite.py",
        "function": "test_cart_icon_points_to_cart_route",
        "title": "Cart icon links to cart route",
        "purpose": "Verify the header cart icon exists and points to a cart route.",
    },
    {
        "path": "tests/navigation/test_navigation_additional_suite.py",
        "function": "test_category_route_renders_product_links_without_server_error",
        "title": "Category route renders product links",
        "purpose": "Verify the category listing page is non-blank, has no server error text, and shows product detail links.",
    },
    {
        "path": "tests/navigation/test_navigation_negative_suite.py",
        "function": "test_invalid_route_is_handled_without_server_error",
        "title": "Invalid route handles gracefully",
        "purpose": "Verify an invalid route does not expose server/runtime error content.",
    },
    # Product
    {
        "path": "tests/product/test_product_detail_edge_suite.py",
        "function": "test_product_detail_price_is_parseable_positive_value",
        "title": "Product detail price is parseable",
        "purpose": "Verify product detail price text can be parsed into a positive value.",
    },
    {
        "path": "tests/product/test_product_detail_edge_suite.py",
        "function": "test_product_detail_add_to_cart_control_exists",
        "title": "Product detail add-to-cart control exists",
        "purpose": "Verify product detail page exposes a visible add-to-cart control.",
    },
    {
        "path": "tests/product/test_product_detail_suite.py",
        "function": "test_view_product_detail",
        "title": "View product detail",
        "purpose": "Verify product detail page shows image, description, and price.",
    },
    # Search / listing
    {
        "path": "tests/search/test_listing_quality_suite.py",
        "function": "test_listing_prices_are_parseable_positive_values",
        "title": "Listing prices are parseable",
        "purpose": "Verify product listing exposes parseable positive price values.",
    },
    {
        "path": "tests/search/test_listing_quality_suite.py",
        "function": "test_listing_product_images_have_valid_sources",
        "title": "Listing product images have valid sources",
        "purpose": "Verify listing product images have usable src or data-src values and are not broken.",
    },
    {
        "path": "tests/search/test_search_edge_cases.py",
        "function": "test_search_unaccented_keywords_are_handled",
        "title": "Search unaccented keywords are handled",
        "purpose": "Verify unaccented keywords 'ao', 'giay', and 'quan' keep the site responsive and free of runtime error text.",
    },
    {
        "path": "tests/search/test_search_edge_cases.py",
        "function": "test_search_accented_keywords_are_handled",
        "title": "Search accented keywords are handled",
        "purpose": "Verify accented keywords 'áo', 'giày', and 'quần' keep the site responsive and free of runtime error text.",
    },
    {
        "path": "tests/search/test_search_edge_cases.py",
        "function": "test_search_keywords_with_surrounding_spaces_are_handled",
        "title": "Search keywords with surrounding spaces are handled",
        "purpose": "Verify keywords with leading/trailing spaces keep the site responsive and free of runtime error text.",
    },
    {
        "path": "tests/search/test_search_edge_cases.py",
        "function": "test_search_special_character_keywords_are_handled",
        "title": "Search special-character keywords are handled",
        "purpose": "Verify special-character search keywords keep the site responsive and free of runtime error text.",
    },
    {
        "path": "tests/search/test_search_listing_suite.py",
        "function": "test_listing_has_clickable_product_detail_links",
        "title": "Listing has clickable product detail links",
        "purpose": "Verify listing product detail links exist and contain valid href values.",
    },
    {
        "path": "tests/search/test_search_suite.py",
        "function": "test_search_product_by_keyword",
        "title": "Search product by keyword",
        "purpose": "Verify keyword search navigates to search listing and returns matching products.",
    },
    {
        "path": "tests/search/test_search_suite.py",
        "function": "test_product_list_display",
        "title": "Product list displays cards",
        "purpose": "Verify product listing shows cards with non-empty name and price content.",
    },
    # UI
    {
        "path": "tests/ui/test_ui_validation_suite.py",
        "function": "test_home_search_input_is_visible",
        "title": "Home search input is visible",
        "purpose": "Verify the search input exists and is visible on the home page.",
    },
    {
        "path": "tests/ui/test_ui_validation_suite.py",
        "function": "test_mobile_viewport_home_page_is_not_blank",
        "title": "Mobile home page is not blank",
        "purpose": "Verify the home page renders non-blank content on a mobile viewport.",
    },
]


def _test_group(case: dict) -> str:
    parts = case["path"].replace("\\", "/").split("/")
    return parts[1] if len(parts) > 1 and parts[0] == "tests" else ""


def _group_sort_key(index_and_case: tuple[int, dict]) -> tuple[int, int]:
    index, case = index_and_case
    group = _test_group(case)
    if group not in GROUP_INDEX:
        raise ValueError(f"Unknown test group for testcase path: {case['path']}")
    return GROUP_INDEX[group], index


def _with_generated_ids(cases: list[dict]) -> list[dict]:
    sorted_cases = [case for _, case in sorted(enumerate(cases), key=_group_sort_key)]
    generated_cases = []
    for index, case in enumerate(sorted_cases, start=1):
        generated_cases.append({**case, "id": f"TC-{index:03d}", "group": _test_group(case)})
    return generated_cases


TEST_CASES = _with_generated_ids(TEST_CASE_DEFINITIONS)


def test_case_key(path: str, function: str, params: dict | None = None) -> tuple:
    normalized_params = tuple(sorted((params or {}).items()))
    return path.replace("\\", "/"), function, normalized_params


TEST_CASE_BY_KEY = {
    test_case_key(case["path"], case["function"], case.get("params")): case
    for case in TEST_CASES
}
