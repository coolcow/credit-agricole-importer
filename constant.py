# --------- CONFIG FILE -------- #
CONFIG_FILE = "config.ini"
# ---------- SETTINGS ---------- #
SETTINGS_SECTION = "GlobalSettings"
SAVE_LOGS_FIELD = "save-logs"
SAVE_LOGS_DEFAULT = "False"
MAX_LOG_FILES_FIELD = "max-log-files"
MAX_LOG_FILES_DEFAULT = "0"
DEBUG_FIELD = "debug"
DEBUG_DEFAULT = "False"
AUTO_DETECT_TRANSFERS_FIELD = "auto-detect-transfers"
AUTO_DETECT_TRANSFERS_DEFAULT = "True"
# --------- CREDIT AGRICOLE -------- #
CREDIT_AGRICOLE_SECTION = "CreditAgricole"
BANK_DEPARTMENT_FIELD = "bank-department"
BANK_DEPARTMENT_DEFAULT = "75"
BANK_ACCOUNT_ID_FIELD = "bank-account-id"
BANK_ACCOUNT_ID_DEFAULT = "XXXXXXXXXXX"
BANK_PASSWORD_FIELD = "bank-password"
BANK_PASSWORD_DEFAULT = "XXXXXX"
IMPORT_ACCOUNT_ID_LIST_FIELD = "import-account-id-list"
IMPORT_ACCOUNT_ID_LIST_DEFAULT = "XXXXXXXXXXX,XXXXXXXXXXX,XXXXXXXXXXX"
GET_TRANSACTIONS_PERIOD_DAYS_FIELD = "get-transactions-period-days"
GET_TRANSACTIONS_PERIOD_DAYS_DEFAULT = "30"
MAX_TRANSACTIONS_PER_GET_FIELD = "max-transactions-per-get"
MAX_TRANSACTIONS_PER_GET_DEFAULT = "100"
# ----------- FIREFLY ---------- #
FIREFLY3_SECTION = "FireflyIII"
ACCOUNTS_NAME_FORMAT_FIELD = "accounts-name-format"
BANK_ACCOUNT_NAME_PLACEHOLDER = "#bank-account-name#"
ACCOUNTS_NAME_FORMAT_DEFAULT = "CREDIT AGRICOLE - " + BANK_ACCOUNT_NAME_PLACEHOLDER
HOSTNAME_FIELD = "hostname"
HOSTNAME_DEFAULT = "https://demo.firefly-iii.org/"
PERSONAL_TOKEN_FIELD = "personal-token"
PERSONAL_TOKEN_DEFAULT = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# ----------- RENAME ----------- #
A_RENAME_TRANSACTION_SECTION = "AutoRenameTransaction"
# ----------- BUDGET ----------- #
AA_BUDGET_SECTION = "AutoAssignBudget"
# ----------- CATEGORY ----------- #
AA_CATEGORY_SECTION = "AutoAssignCategory"
# ----------- ACCOUNT ----------- #
AA_ACCOUNT_SECTION = "AutoAssignAccount"
# ----------- TAGS ----------- #
AA_TAGS_SECTION = "AutoAssignTags"
