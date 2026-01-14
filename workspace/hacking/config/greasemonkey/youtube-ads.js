// ==UserScript==
// @name Nuclear YouTube Ad Skipper
// @description Aggressively skips ALL YouTube ads
// @run-at document-start
// @match *://*.youtube.com/*
// @match *://youtube.com/*
// @grant none
// ==/UserScript==

(function() {
    'use strict';
    
    console.log('🚀 Nuclear YouTube Ad Blocker Activated!');
    
    // ALL known ad selectors - updated December 2024
    const AD_SELECTORS = [
        // Skip buttons
        '.videoAdUiSkipButton',
        '.ytp-ad-skip-button-modern',
        '.ytp-ad-skip-button',
        '.ytp-ad-skip-button-container',
        '.ytp-ad-skip-button-slot',
        '.ytp-skip-ad-button',
        
        // Ad containers
        '.ad-showing',
        '.ad-interrupting',
        '.ytp-ad-player-overlay',
        '.ytp-ad-image-overlay',
        '.ytp-ad-text-overlay',
        '.ytp-ad-message-overlay',
        '.ytp-ad-action-interstitial',
        
        // YouTube ad elements
        'ytd-ad-slot-renderer',
        'ytd-display-ad-renderer',
        'ytd-promoted-sparkles-web-renderer',
        'ytd-action-companion-ad-renderer',
        'ytd-in-feed-ad-layout-renderer',
        'ytd-banner-promo-renderer',
        'ytd-compact-promoted-video-renderer',
        
        // General ad classes
        '.companion-ad-container',
        '.ad-container',
        '.ad-div',
        '.ad-unit',
        '.video-ads',
        '.ytp-ad-module',
        '.ytd-player-legacy-desktop-watch-ads-renderer',
        
        // Attributes containing "ad"
        '[class*="ad-"]',
        '[id*="ad-"]',
        '[aria-label*="advertisement"]',
        '[data-ad-]',
        '[data-target="ad-"]',
        
        // Premium/Sponsor prompts
        '.ytp-paid-content-overlay',
        '.ytp-sponsor-segment',
        '.sponsor-block-overlay',
        
        // New YouTube 2024 ad elements
        '.ytp-ad-text',
        '.ytp-ad-progress',
        '.ytp-ad-info-dialog-container',
        '.ytp-ad-info-preview-container',
        '.ytp-ad-info-panel-container',
        
        // Masthead ads
        'ytd-masthead-ad-creative-renderer',
        '#masthead-ad',
        '.masthead-ad-control'
    ];
    
    // YouTube ad/tracking domains to block
    const BLOCKED_DOMAINS = [
        'doubleclick.net',
        'googlesyndication.com',
        'googleadservices.com',
        'adservice.google.com',
        'ads.youtube.com',
        'googleads.g.doubleclick.net',
        'youtube.com/api/stats/ads',
        'youtube.com/pagead/',
        'youtube.com/ptracking',
        'youtube.com/get_midroll_',
        'youtube.com/api/stats/qoe',
        'youtube.com/youtubei/v1/log_event',
        'google-analytics.com',
        'googletagmanager.com',
        'gstatic.com/ad',
        'ggpht.com/ad'
    ];
    
    // ===== NUCLEAR FUNCTIONS =====
    
    // 1. CLICK ALL SKIP BUTTONS
    function clickAllSkipButtons() {
        AD_SELECTORS.forEach(selector => {
            try {
                document.querySelectorAll(selector).forEach(btn => {
                    if (btn && btn.click) {
                        btn.click();
                        console.log('✅ Clicked:', selector);
                        
                        // Force skip video ads
                        if (selector.includes('skip') || selector.includes('Skip')) {
                            const video = document.querySelector('video');
                            if (video) {
                                video.currentTime = video.duration || 999999;
                                video.playbackRate = 16; // Speed through ads
                            }
                        }
                    }
                });
            } catch (e) {}
        });
    }
    
    // 2. REMOVE ALL AD CONTAINERS
    function removeAllAdContainers() {
        AD_SELECTORS.forEach(selector => {
            try {
                document.querySelectorAll(selector).forEach(element => {
                    // Nuclear removal
                    element.style.cssText = `
                        display: none !important;
                        visibility: hidden !important;
                        opacity: 0 !important;
                        height: 0 !important;
                        width: 0 !important;
                        position: absolute !important;
                        left: -9999px !important;
                        pointer-events: none !important;
                        z-index: -9999 !important;
                    `;
                    
                    // Remove from DOM completely
                    if (element.parentNode) {
                        element.parentNode.removeChild(element);
                    }
                    
                    // Remove event listeners
                    element.replaceWith(element.cloneNode(true));
                });
            } catch (e) {}
        });
    }
    
    // 3. SKIP VIDEO ADS
    function skipVideoAds() {
        const videos = document.querySelectorAll('video');
        videos.forEach(video => {
            // Check if this is an ad video
            const isAd = () => {
                // Check parent elements for ad classes
                let parent = video;
                for (let i = 0; i < 5; i++) {
                    parent = parent.parentElement;
                    if (!parent) break;
                    
                    const classes = parent.className || '';
                    const id = parent.id || '';
                    
                    if (classes.includes('ad-') || 
                        id.includes('ad-') || 
                        classes.includes('ad_') ||
                        AD_SELECTORS.some(selector => parent.matches?.(selector))) {
                        return true;
                    }
                }
                return false;
            };
            
            if (isAd()) {
                console.log('🚫 AD VIDEO DETECTED - SKIPPING');
                
                // Nuclear skip
                video.currentTime = video.duration || 999999999;
                video.playbackRate = 16;
                video.volume = 0;
                video.muted = true;
                
                // Prevent ad from playing
                video.pause();
                
                // Try to restore normal video
                setTimeout(() => {
                    const mainVideo = document.querySelector('video:not([class*="ad-"])');
                    if (mainVideo) {
                        mainVideo.currentTime = 0;
                        mainVideo.play();
                    }
                }, 100);
            }
        });
    }
    
    // 4. BLOCK AD NETWORK REQUESTS
    function blockAdRequests() {
        // Block fetch requests
        const originalFetch = window.fetch;
        window.fetch = function(...args) {
            const url = args[0]?.url || args[0] || '';
            if (BLOCKED_DOMAINS.some(domain => url.includes(domain))) {
                console.log('🚫 Blocked fetch:', url.substring(0, 100));
                return Promise.reject(new Error('YouTube Ad Blocker: Request blocked'));
            }
            return originalFetch.apply(this, args);
        };
        
        // Block XMLHttpRequest
        const originalXHROpen = XMLHttpRequest.prototype.open;
        XMLHttpRequest.prototype.open = function(method, url) {
            if (BLOCKED_DOMAINS.some(domain => url.includes(domain))) {
                console.log('🚫 Blocked XHR:', url.substring(0, 100));
                this._blocked = true;
                return;
            }
            return originalXHROpen.apply(this, arguments);
        };
        
        // Block WebSocket connections to ad servers
        const originalWebSocket = window.WebSocket;
        window.WebSocket = function(url, protocols) {
            if (BLOCKED_DOMAINS.some(domain => url.includes(domain))) {
                console.log('🚫 Blocked WebSocket:', url);
                throw new Error('YouTube Ad Blocker: WebSocket blocked');
            }
            return new originalWebSocket(url, protocols);
        };
    }
    
    // 5. MUTATION OBSERVER - Catch dynamically loaded ads
    function setupMutationObserver() {
        const observer = new MutationObserver((mutations) => {
            let adsDetected = false;
            
            mutations.forEach(mutation => {
                // Check added nodes
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === 1) { // Element node
                        const element = node;
                        AD_SELECTORS.forEach(selector => {
                            if (element.matches?.(selector) || 
                                element.querySelector?.(selector)) {
                                adsDetected = true;
                            }
                        });
                    }
                });
                
                // Check attribute changes (for classes like 'ad-showing')
                if (mutation.type === 'attributes' && 
                    (mutation.attributeName === 'class' || mutation.attributeName === 'id')) {
                    const target = mutation.target;
                    AD_SELECTORS.forEach(selector => {
                        if (target.matches?.(selector)) {
                            adsDetected = true;
                        }
                    });
                }
            });
            
            if (adsDetected) {
                console.log('🔍 Mutation detected - cleaning ads');
                clickAllSkipButtons();
                skipVideoAds();
                removeAllAdContainers();
            }
        });
        
        // Start observing everything
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['class', 'id', 'style', 'src']
        });
        
        return observer;
    }
    
    // 6. VIDEO EVENT LISTENERS
    function setupVideoListeners() {
        document.addEventListener('playing', (e) => {
            if (e.target.tagName === 'VIDEO') {
                setTimeout(skipVideoAds, 100);
            }
        });
        
        document.addEventListener('timeupdate', (e) => {
            if (e.target.tagName === 'VIDEO') {
                const video = e.target;
                // If video is at beginning and looks like an ad, skip it
                if (video.currentTime < 2 && video.duration < 60) {
                    skipVideoAds();
                }
            }
        });
        
        document.addEventListener('canplay', skipVideoAds);
        document.addEventListener('loadeddata', skipVideoAds);
    }
    
    // 7. PERIODIC CLEANUP (in case something slips through)
    function startPeriodicCleanup() {
        // Fast cleanup for first 30 seconds (when ads usually appear)
        let fastCleanup = setInterval(() => {
            clickAllSkipButtons();
            skipVideoAds();
            removeAllAdContainers();
        }, 250); // Every 250ms - aggressive!
        
        // Stop fast cleanup after 30 seconds
        setTimeout(() => {
            clearInterval(fastCleanup);
            console.log('⏱️ Fast cleanup stopped');
        }, 30000);
        
        // Regular cleanup continues forever
        setInterval(() => {
            clickAllSkipButtons();
            skipVideoAds();
            removeAllAdContainers();
        }, 1000); // Every second
    }
    
    // 8. PREVENT ADBLOCK DETECTION
    function preventAdblockDetection() {
        // Spoof ad-related variables
        Object.defineProperty(window, 'adsbygoogle', { value: [] });
        Object.defineProperty(window, 'google_ad', { value: {} });
        Object.defineProperty(window, 'google_ads', { value: {} });
        
        // Mock ad elements if they're checked for existence
        const mockAdElement = {
            style: {},
            parentNode: null,
            appendChild: () => {},
            removeChild: () => {}
        };
        
        // Intercept getElementById for ad elements
        const originalGetElementById = document.getElementById;
        document.getElementById = function(id) {
            if (id && id.includes('ad') || id.includes('Ad') || id.includes('AD')) {
                console.log('🛡️ Spoofed ad element request:', id);
                return mockAdElement;
            }
            return originalGetElementById.call(document, id);
        };
    }
    
    // ===== MAIN INITIALIZATION =====
    function initNuclearAdBlocker() {
        console.log('💣 INITIALIZING NUCLEAR YOUTUBE AD BLOCKER');
        
        // Block network requests first
        blockAdRequests();
        preventAdblockDetection();
        
        // Initial cleanup
        clickAllSkipButtons();
        skipVideoAds();
        removeAllAdContainers();
        
        // Setup observers and listeners
        setupMutationObserver();
        setupVideoListeners();
        startPeriodicCleanup();
        
        console.log('✅ Nuclear YouTube Ad Blocker fully operational');
        
        // Send message to qutebrowser
        if (typeof qute !== 'undefined') {
            qute.command('message-info "Nuclear ad blocker activated!"');
        }
    }
    
    // Run when page is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initNuclearAdBlocker);
    } else {
        initNuclearAdBlocker();
    }
    
    // Also run on YouTube's AJAX navigation
    document.addEventListener('yt-navigate-finish', initNuclearAdBlocker);
    document.addEventListener('spfdone', initNuclearAdBlocker); // Old YouTube
    document.addEventListener('yt-page-data-updated', initNuclearAdBlocker);
    
})();
