from helpers import sessionMaker
from database_setup import User, Employer, Job, Category

session = sessionMaker.newSession()


# Create dummy user
User1 = User(name="Anthony Sarkis", email="anthonysarkis@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Category labels
category1 = Category(id=1, name="Software Developement")
category2 = Category(id=2, name="Healthcare")
category3 = Category(id=3, name="Sales")
category4 = Category(id=4, name="Food Service")

session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.commit()


# Menu for Super Stir Fry
employer2 = Employer(user_id=1, name="Buber")

session.add(employer2)
session.commit()


job1 = Job(user_id=1, header="Driver", description="Drive our cars",
           salary="Peanuts", category_id=2, employer=employer2)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Lots of ducks",
           description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", salary="$25", category_id=2, employer=employer2)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
           salary="15", category_id=2, employer=employer2)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
           salary="12", category_id=2, employer=employer2)

session.add(job4)
session.commit()

job5 = Job(user_id=1, header="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
           salary="14", category_id=2, employer=employer2)

session.add(job5)
session.commit()

job6 = Job(user_id=1, header="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
           salary="12", category_id=2, employer=employer2)

session.add(job6)
session.commit()


# Menu for Panda Garden
employer1 = Employer(user_id=1, name="Panda Garden")

session.add(employer1)
session.commit()


job1 = Job(user_id=1, header="Pho", description="a Vietheaderse noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
           salary="$8.99", category_id=2, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
           salary="$6.99", category_id=1, employer=employer1)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
           salary="$9.95", category_id=2, employer=employer1)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
           salary="$6.99", category_id=2, employer=employer1)

session.add(job4)
session.commit()

job2 = Job(user_id=1, header="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
           salary="$9.50", category_id=2, employer=employer1)

session.add(job2)
session.commit()


# Menu for Thyme for that
employer1 = Employer(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(employer1)
session.commit()


job1 = Job(user_id=1, header="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
           salary="$2.99", category_id=3, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
           salary="$5.99", category_id=2, employer=employer1)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header="Honey Boba Shaved Snow",
           description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", salary="$4.50", category_id=3, employer=employer1)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
           salary="$6.95", category_id=1, employer=employer1)

session.add(job4)
session.commit()

job5 = Job(user_id=1, header="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
           salary="$7.95", category_id=2, employer=employer1)

session.add(job5)
session.commit()

job2 = Job(user_id=1, header="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
           salary="$6.80", category_id=2, employer=employer1)

session.add(job2)
session.commit()


# Menu for Tony's Bistro
employer1 = Employer(user_id=1, name="Tony\'s Bistro ")

session.add(employer1)
session.commit()


job1 = Job(user_id=1, header="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
           salary="$13.95", category_id=2, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Chicken and Rice", description="Chicken... and rice",
           salary="$4.95", category_id=2, employer=employer1)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
           salary="$6.95", category_id=2, employer=employer1)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
           description="Milk, cream, salt, ..., Liquid nitrogen magic", salary="$3.95", category_id=3, employer=employer1)

session.add(job4)
session.commit()

job5 = Job(user_id=1, header="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
           salary="$7.95", category_id=2, employer=employer1)

session.add(job5)
session.commit()


# Menu for Andala's
employer1 = Employer(user_id=1, name="Andala\'s")

session.add(employer1)
session.commit()


job1 = Job(user_id=1, header="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
           salary="$9.95", category_id=2, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
           salary="$7.95", category_id=2, employer=employer1)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
           salary="$6.50", category_id=1, employer=employer1)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
           salary="$6.75", category_id=1, employer=employer1)

session.add(job4)
session.commit()

job2 = Job(user_id=1, header="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
           salary="$7.00", category_id=2, employer=employer1)

session.add(job2)
session.commit()


# Menu for Auntie Ann's
employer1 = Employer(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(employer1)
session.commit()

job9 = Job(user_id=1, header="Chicken Fried Steak",
           description="Fresh battered sirloin steak fried and smothered with cream gravy", salary="$8.99", category_id=2, employer=employer1)

session.add(job9)
session.commit()


job1 = Job(user_id=1, header="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
           salary="$2.99", category_id=3, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
           salary="$10.95", category_id=2, employer=employer1)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header="Morels on toast (seasonal)",
           description="Wild morel mushrooms fried in butter, served on herbed toast slices", salary="$7.50", category_id=1, employer=employer1)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
           salary="$8.95", category_id=2, employer=employer1)

session.add(job4)
session.commit()

job2 = Job(user_id=1, header="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
           salary="$9.50", category_id=2, employer=employer1)

session.add(job2)
session.commit()

job10 = Job(user_id=1, header="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
            salary="$1.99", category_id=3, employer=employer1)

session.add(job10)
session.commit()


# Menu for Cocina Y Amor
employer1 = Employer(user_id=1, name="Cocina Y Amor ")

session.add(employer1)
session.commit()


job1 = Job(user_id=1, header="Super Burrito Al Pastor",
           description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", salary="$5.95", category_id=2, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
           salary="$7.99", category_id=2, employer=employer1)

session.add(job2)
session.commit()


employer1 = Employer(user_id=1, name="State Bird Provisions")
session.add(employer1)
session.commit()

job1 = Job(user_id=1, header="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
           salary="$5.95", category_id=1, employer=employer1)

session.add(job1)
session.commit

job1 = Job(user_id=1, header="Guanciale Chawanmushi",
           description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", salary="$6.95", category_id=3, employer=employer1)

session.add(job1)
session.commit()


job1 = Job(user_id=1, header="Lemon Curd Ice Cream Sandwich",
           description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", salary="$4.25", category_id=3, employer=employer1)

session.add(job1)
session.commit()


# Menu for Hooli
employer1 = Employer(user_id=1, name="Hooli")

session.add(employer1)
session.commit()

job2 = Job(user_id=1, header="Python Developer", description="We are seeking skilled Java Developers to join our Winnipeg team. You will engage with numerous different clients and amazing development teams to design, estimate, code, and test complex programs.",
           salary="$20,000", category_id=1, employer=employer1)

session.add(job2)
session.commit()


job1 = Job(user_id=1, header="JavaScript Developer", description="Work closely with fellow Software Engineers and members of other disciplines on the project team. HB Studios is the largest video game developer in Atlantic...",
           salary="$10,000", category_id=1, employer=employer1)

session.add(job1)
session.commit()

job2 = Job(user_id=1, header="C++ Developer", description="Software Development Company. AGILE software development methodology Must Have Primary Skills :. AGILE software development methodology Nice To Have Secondary..",
           salary="$10/hour", category_id=1, employer=employer1)

session.add(job2)
session.commit()

job3 = Job(user_id=1, header=".Net Developer", description="Complete development-related tasks as assigned by tech leads and/or senior developers. Software development - .NET 4.0 and prior versions / C# / SQL Server and..",
           salary="TBD", category_id=1, employer=employer1)

session.add(job3)
session.commit()

job4 = Job(user_id=1, header="C# Developer", description="These tasks are applicable to new systems development, system enhancement and external software packages. Tracks and monitors the performance of current and/or...",
           salary="TBD", category_id=1, employer=employer1)

session.add(job4)
session.commit()

job5 = Job(user_id=1, header="Ruby Developer", description="Test driven development and the use of version control software should be familiar to the candidate. Our Regina, SK based client is looking for full time Java...",
           salary="TBD", category_id=1, employer=employer1)

session.add(job5)
session.commit()

job6 = Job(user_id=1, header="Product Manager", description="Engineered Code is looking for an experienced software developer who can manage a team building websites and software applications..",
           salary="$30,000", category_id=4, employer=employer1)

session.add(job6)
session.commit()

job7 = Job(user_id=1, header="Product Director",
           description="Engineered Code is looking for an experienced software developer who can manage a team building websites and software applications..", salary="$100,000", category_id=2, employer=employer1)

session.add(job7)
session.commit()


print "added a user, employers, and jobs!"
