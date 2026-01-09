# ===== BASIC CONFIGURATION =====
config.load_autoconfig(False)

# ===== SPECIAL KEYS =====
# Make F13 behave exactly like Escape in every mode
config.bind('<F13>', 'mode-leave', mode='insert')
config.bind('<F13>', 'fake-key <Escape>', mode='normal')
config.bind('<F13>', 'fake-key <Escape>', mode='passthrough')
config.bind('<F13>', 'fake-key <Escape>', mode='command')
config.bind('<F13>', 'fake-key <Escape>', mode='caret')
config.bind('<F13>', 'fake-key <Escape>', mode='hint')

# ===== CORE COLOR SETTINGS =====
config.load_autoconfig()
config.set('content.user_stylesheets', ['~/.config/qutebrowser/green-black.css'])

# Corrected single toggle key
config.bind(',st', 
    'config-cycle content.user_stylesheets [] ["~/.config/qutebrowser/green-black.css"] ;; ' +
    'jseval -q py:message.info("Green/Black theme " + ' +
    '("ENABLED" if config.val.content.user_stylesheets else "DISABLED"))',
    mode='normal')

# Text colors (All green #00FF4C)
c.colors.completion.fg = '#00FF4C'
c.colors.completion.category.fg = '#00FF4C'
c.colors.statusbar.normal.fg = '#00FF4C'
c.colors.statusbar.insert.fg = '#00FF4C'
c.colors.statusbar.command.fg = '#00FF4C'
c.colors.statusbar.url.fg = '#00FF4C'
c.colors.hints.fg = '#00FF4C'
c.colors.contextmenu.menu.fg = '#00FF4C'

# Background colors (All black #000000)
c.colors.completion.category.bg = '#000000'
c.colors.completion.odd.bg = '#000000'
c.colors.completion.even.bg = '#000000'
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.insert.bg = '#000000'
c.colors.statusbar.command.bg = '#000000'
c.colors.tabs.bar.bg = '#000000'
c.colors.hints.bg = '#000000'
c.colors.contextmenu.menu.bg = '#000000'

# ===== TAB COLORS =====
# Selected tab (green background, black text)
c.colors.tabs.selected.odd.fg = '#000000'
c.colors.tabs.selected.odd.bg = '#00FF4C'
c.colors.tabs.selected.even.fg = '#000000'
c.colors.tabs.selected.even.bg = '#00FF4C'

# Other tabs (black background, green text)
c.colors.tabs.odd.fg = '#00FF4C'
c.colors.tabs.odd.bg = '#000000'
c.colors.tabs.even.fg = '#00FF4C'
c.colors.tabs.even.bg = '#000000'

# Context menu selection
c.colors.contextmenu.selected.fg = '#000000'
c.colors.contextmenu.selected.bg = '#00FF4C'

# ===== SIDEBAR CONFIGURATION =====
c.tabs.position = 'left'
c.tabs.show = 'always'
c.tabs.width = '12%'
c.tabs.indicator.width = 0  # No tab underline
c.tabs.padding = {'bottom': 2, 'left': 2, 'right': 2, 'top': 2}
c.tabs.title.alignment = 'left'
c.tabs.favicons.show = 'always'
c.tabs.min_width = 80
c.tabs.max_width = 150

# ===== FONT SETTINGS =====
c.fonts.default_family = 'monospace'
c.fonts.default_size = '11pt'
c.fonts.tabs.selected = '11pt monospace'
c.fonts.tabs.unselected = '11pt monospace'
c.fonts.statusbar = '11pt monospace'
c.fonts.hints = 'bold 11pt monospace'

# ===== WEB CONTENT SETTINGS =====
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.bg = 'black'

# ===== START PAGES =====
c.url.start_pages = ['https://blank.page/']
c.url.default_page = 'https://blank.page/'

# ===== DARK MODE POLICY =====
# Disabled to prevent conflicts with our CSS
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.darkmode.policy.page = 'always'

# ===== IMPROVED SESSION MANAGEMENT =====
# Save session with name prompt
config.bind(',ws', 'set-cmd-text -s :session-save')
config.bind(',wS', 'set-cmd-text -s :session-save -o')  # Overwrite existing

# Load session with name prompt
config.bind(',wl', 'set-cmd-text -s :session-load')
config.bind(',wL', 'set-cmd-text -s :session-load -t')  # Load in new window

# Quick session slots (for frequently used sessions)
config.bind(',w1', 'session-save work1')
config.bind(',w2', 'session-save work2') 
config.bind(',w3', 'session-save work3')
config.bind(',w4', 'session-save personal')
config.bind(',w5', 'session-save temp')

config.bind(',l1', 'session-load work1 ;; close')
config.bind(',l2', 'session-load work2 ;; close')
config.bind(',l3', 'session-load work3 ;; close')
config.bind(',l4', 'session-load personal ;; close')
config.bind(',l5', 'session-load temp ;; close')

# Session management commands
config.bind(',wd', 'set-cmd-text -s :session-delete')  # Delete session
config.bind(',wL', 'session-list')  # List all saved sessions

# Auto-save current session periodically
c.auto_save.interval = 30000  # Save every 30 seconds (optional)
c.auto_save.session = True

# ===== MULTI-WINDOW SESSION SUPPORT =====
c.session.lazy_restore = True  # Don't restore until needed

# ===== SESSION STORAGE LOCATION =====
import os
session_dir = os.path.expanduser('~/.local/share/qutebrowser/sessions')
os.makedirs(session_dir, exist_ok=True)

# ===== TAB MANAGEMENT =====
config.bind(',tg', 'tab-give')
config.bind(',tn', 'tab-focus next')
config.bind(',tp', 'tab-focus prev')
config.bind(',tm', 'tab-move')

# ===== WORKSPACE MANAGEMENT =====
config.bind(',wd1', 'spawn --userscript switch-workspace hacking')
config.bind(',wd2', 'spawn --userscript switch-workspace study')
config.bind(',wd3', 'spawn --userscript switch-workspace z6')

# Opens new workspace while keeping current window open (capital W)
config.bind(',W1', 'spawn --userscript open-workspace hacking')
config.bind(',W2', 'spawn --userscript open-workspace study')
config.bind(',W3', 'spawn --userscript open-workspace z6')

# ===== BRAVE-LEVEL ADBLOCKING CONFIGURATION =====
# Enable ad-blocking system
c.content.blocking.enabled = True

# Blocking method - use 'both' for maximum protection
c.content.blocking.method = 'both'

# ===== AGGRESSIVE ADBLOCK LISTS (Brave-like protection) =====
c.content.blocking.adblock.lists = [
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2024.txt',
    'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/YouTubeAdblockList.txt',
    'https://raw.githubusercontent.com/Mechazawa/FuckFuckAdblock/master/FuckFuckAdblock.txt',
    'https://raw.githubusercontent.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt',
    'https://easylist.to/easylist/easylist.txt',
    'https://easylist.to/easylist/easyprivacy.txt',
    'https://easylist-downloads.adblockplus.org/easylist.txt',
    'https://secure.fanboy.co.nz/fanboy-annoyance.txt',
    'https://easylist.to/easylist/fanboy-social.txt',
    'https://www.i-dont-care-about-cookies.eu/abp/',
    'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers.txt',
    'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/tracking.txt',
    'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/MobileFilter/sections/adservers.txt',
    'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt',
    'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt',
    'https://easylist-downloads.adblockplus.org/easylistitaly.txt',
    'https://stanev.org/abp/adblock_bg.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-standard.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-disconnect.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-cookie-consent.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-firstparty.txt',
    'https://raw.githubusercontent.com/brave/adblock-lists/master/region/usa.txt',  # USA
    'https://raw.githubusercontent.com/brave/adblock-lists/master/region/eur.txt',  # Europe
    'https://raw.githubusercontent.com/brave/adblock-lists/master/region/jpn.txt',  # Japan
    'https://raw.githubusercontent.com/brave/adblock-lists/master/brave-social.txt',
]

# ===== AGGRESSIVE HOSTS-BASED BLOCKING =====
c.content.blocking.hosts.lists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://someonewhocares.org/hosts/zero/hosts',
    'https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt',
    'https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt',
    'https://raw.githubusercontent.com/jmdugan/blocklists/master/corporations/facebook/all',
    'https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt',

]

# ===== BRAVE-LIKE PRIVACY SETTINGS =====
# Cookie control (Brave blocks 3rd-party cookies by default)
c.content.cookies.accept = 'no-3rdparty'

# Fingerprint protection
c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
c.content.headers.custom = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

# Do Not Track
c.content.headers.do_not_track = True

# Block JavaScript popups and redirects
c.content.javascript.modal_dialog = False
c.content.javascript.can_open_tabs_automatically = False

# WebRTC blocking (prevents IP leaks)
c.content.webrtc_ip_handling_policy = 'disable-non-proxied-udp'

# Block autoplay videos
c.content.autoplay = False

# ===== ENHANCED ADBLOCK KEYBINDS =====
config.bind(',au', 'adblock-update', mode='normal')  # Update blocklists
config.bind(',at', 'adblock-toggle', mode='normal')  # Toggle ad-blocking
config.bind(',al', 'adblock-list', mode='normal')  # Show blocked elements

# Quick whitelist current site
config.bind(',aw', 'adblock-whitelist ;; message-info "Site whitelisted"', mode='normal')

# Toggle JavaScript (like Brave's shields)
config.bind(',aj', 'config-cycle content.javascript.enabled true false ;; reload',
            mode='normal')

# Quick toggle for aggressive blocking
config.bind(',aa', 'config-cycle content.blocking.method both auto ;; message-info "Adblock method: {}"'.format('{value}'),
            mode='normal')

# ===== CUSTOM SITE EXCEPTIONS (for broken sites) =====
c.content.blocking.whitelist = [
    # Add sites that break with aggressive blocking
    # Example: '*.youtube.com',  # If you need YouTube to work differently
    # '*.google.com',   # If search breaks
    # '*.paypal.com',   # Financial sites often need exceptions
]

# ===== AUTOMATIC UPDATES =====
# Update blocklists automatically (every 24 hours)
c.content.blocking.adblock.update_interval = 24 * 60 * 60  # Seconds

# ===== PERFORMANCE OPTIMIZATIONS =====
# Cache adblock rules for faster loading
c.content.blocking.adblock.cache = True

# ===== CONTENT SETTINGS FOR BETTER BLOCKING =====
# Block images from 3rd party sites by default
c.content.images = True
config.bind(',ai', 'config-cycle content.images true false ;; reload',
            mode='normal')

# Block media autoplay
c.content.media.audio_video_capture = False
c.content.media.audio_capture = False
c.content.media.video_capture = False
c.content.media.media_keys = False

# ===== MISCELLANEOUS SETTINGS =====
# Default session
c.session.default_name = 'default'

# Downloads
c.downloads.location.directory = '~/Downloads'
c.downloads.location.prompt = False
c.downloads.remove_finished = 3000  # Remove finished downloads after 3 seconds

# Search engines
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'g': 'https://www.google.com/search?q={}',
    'd': 'https://duckduckgo.com/?q={}',
    'y': 'https://www.youtube.com/results?search_query={}',
    'w': 'https://en.wikipedia.org/wiki/{}',
    'r': 'https://www.reddit.com/search?q={}',
    'gh': 'https://github.com/search?q={}',
}

# Enable smooth scrolling
c.scrolling.smooth = True

# Enable hints
c.hints.chars = 'asdfghjkl'

# Status bar settings
c.statusbar.show = 'always'
c.statusbar.position = 'bottom'

# Completion settings
c.completion.height = '30%'
c.completion.shrink = True
c.completion.use_best_match = True

# ===== SECURITY ENHANCEMENTS =====
# Disable dangerous features
c.content.local_content_can_access_remote_urls = False
c.content.local_content_can_access_file_urls = False
c.content.webgl = False

# PDF viewer
c.content.pdfjs = True

# ===== SESSION AUTO-SAVE =====
c.auto_save.session = True
