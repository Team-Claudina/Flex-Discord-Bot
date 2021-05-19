# Rules are created and sorted in the order that they are inserted in the code
rules = [
    # Format is [Str: Rule, Str: Rule Description, Bool: Inline]
    # Eg ['rule-1', 'Don't Do This', False]
    ['Rule 1', 'Have Fun', False],
    ['Rule 2', 'Be Nice', False],
    ['Rule 3', 'Play', False],
    ['Rule 4', 'idk', False]
]

# Servers are created and sorted in the order that they are inserted in the code
servers = [
    # Format is [Str: Server Name, Str: Server Description, Bool: Inline]
    # Eg ['Flex Serv', 'Flex Bot Production', True]
    ['Flex Server', 'Our Website And Hosting', True],
    ['Github', 'Our Github Page At https://github.com/GreyStinger/Flex-Discord-Bot', True]
]

# Static builds need their own list item in the same formatting as what the current ones are.
# Static Builds:
static_builds = {
    'Rules': ['Please Read These Carefully', rules],
    'Servers': ['These are our currently hosted servers.', servers]
}
