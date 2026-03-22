from selenium.webdriver.common.by import By


class FeedPageLocators():
    orders_feed_title = [By.XPATH, ".//*[contains(text(), 'Лента заказов')]"]
    first_order_button = [By.XPATH, "(//*[@class='OrderFeed_list__OLh59'])[1]"]
    text_order = [By.XPATH, ".//*[@class='text text_type_digits-default']"]
    counter_completed_for_all_time = [By.XPATH, ".//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[1]"]
    counter_completed_today = [By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[1]"]
    id_order_at_work = [By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']"]
    