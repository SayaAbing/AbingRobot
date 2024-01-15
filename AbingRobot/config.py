class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 14920143
    API_HASH = "5a316e55fb121d9b5e891b5ff07d4677"

    CASH_API_KEY = "U6Z2DE9I2ZRT4E2A"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ymiitban:qOoRlw3gILCP2hAcJvks0DLw1ODidX98@drona.db.elephantsql.com/ymiitban"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002128110291)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://AbingRobot:garing225@abingrobot.t047arw.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/23896028168d6e96f9255.jpg"

    SUPPORT_CHAT = "ab1ngsupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6830506577:AAHnNtx0_g9knmarXIUXobHUyqAtv9D7PMY"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "ZJWCFKAR78LI"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1715037142  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
