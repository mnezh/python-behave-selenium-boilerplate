from behave import given, when, then


@given(u'I am at google')
def open_google(context):
    context.app.open_google()


@when(u'I search for "{stuff}"')
def search_stuff(context, stuff):
    context.app.search('stuff')


@then(u'I see "{stuff}" in results')
def check_stuff(context, stuff):
    first = context.app.get_first_result().lower()
    assert stuff in first
