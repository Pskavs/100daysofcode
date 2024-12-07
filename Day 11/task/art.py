logo = r"""
__________.__                 __          ____.              __    
\______   \  | _____    ____ |  | __     |    |____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /     |    \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    <  /\__|    |/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \ \________(____  /\___  >__|_ \
        \/          \/     \/     \/               \/     \/     \/
.------.            
|A_  _ |.          
|( \/ ).-----.  Welcome to my blackjack project!
| \  /|K /\  |    By - Christian Paskevicius 
|  \/ | /  \ |     
`-----| \  / |     
      |  \/ K|                     
      `------'          
"""

card_art ={
    "2": """
 _________ 
|2        |
|    ♠    |
|         |
|    ♠    |
|________2|
""",
    "3": """
 _________ 
|3        |
|    ♠    |
|    ♠    |
|    ♠    |
|________3|
""",
    "4": """
 _________ 
|4        |
|  ♠   ♠  |
|         |
|  ♠   ♠  |
|________4|
""",
    "5": """
 _________ 
|5        |
|  ♠   ♠  |
|    ♠    |
|  ♠   ♠  |
|________5|
""",
    "6": """
 _________ 
|6        |
|  ♠   ♠  |
|  ♠   ♠  |
|  ♠   ♠  |
|________6|
""",
    "7": """
 _________ 
|7        |
|  ♠   ♠  |
|  ♠ ♠ ♠  |
|  ♠   ♠  |
|________7|
""",
    "8": """
 _________ 
|8        |
|  ♠ ♠ ♠  |
|  ♠   ♠  |
|  ♠ ♠ ♠  |
|________8|
""",
    "9": """
 _________ 
|9        |
|  ♠ ♠ ♠  |
|  ♠ ♠ ♠  |
|  ♠ ♠ ♠  |
|________9|
""",
    "10": """
 _________ 
|10       |
| ♠ ♠ ♠ ♠ |
|    ♠    |
| ♠ ♠ ♠ ♠ |
|_______10|
""",
    "J": """
 _________ 
|J        |
|    ♠    |
|  JACK   |
|    ♠    |
|________J|
""",
    "Q": """
 _________ 
|Q        |
|    ♠    |
|  QUEEN  |
|    ♠    |
|________Q|
""",
    "K": """
 _________ 
|K        |
|    ♠    |
|  KING   |
|    ♠    |
|________K|
""",
    "A": """
 _________ 
|A        |
|         |
|    ♠    |
|         |
|________A|
"""
}
unknown_card = """
 Face Down
 _________ 
|░░░░░░░░░|
|░░░░░░░░░|
|░░░░░░░░░|
|░░░░░░░░░|
|_________|
"""