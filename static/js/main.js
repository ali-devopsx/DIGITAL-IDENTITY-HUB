/**
 * Main JavaScript File - Digital Identity Hub
 * 
 * Features:
 * - Animated typing effect for hero section
 * - Smooth scrolling and navigation
 * - Contact form handling
 * - Hamburger menu for mobile
 * - Scroll animations
 */

// ============================================================================
// Typing Animation Effect
// ============================================================================

/**
 * Creates an animated typing effect with multiple words that cycle
 * Words fade out and new ones are typed in their place
 */
function initTypingEffect() {
    const typingElement = document.getElementById('typing');
    
    if (!typingElement) return;
    
    // Array of words to cycle through
    const words = ['a Developer', 'a Designer', 'an Innovator', 'a Problem Solver'];
    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let isWaiting = false;
    
    /**
     * Main typing animation loop
     * Types characters one at a time, waits, then deletes
     */
    function type() {
        const currentWord = words[wordIndex];
        const displayText = currentWord.substring(0, charIndex);
        
        typingElement.textContent = displayText;
        
        // Typing speed
        let speed = 100;
        
        if (!isDeleting) {
            // Typing phase
            charIndex++;
            
            if (charIndex === currentWord.length) {
                // Word is complete, wait before deleting
                isWaiting = true;
                setTimeout(() => {
                    isWaiting = false;
                    isDeleting = true;
                    type();
                }, 2000); // Wait 2 seconds before deleting
                return;
            }
        } else {
            // Deleting phase
            charIndex--;
            speed = 50; // Faster deletion
            
            if (charIndex === 0) {
                // All deleted, move to next word
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
            }
        }
        
        if (!isWaiting) {
            setTimeout(type, speed);
        }
    }
    
    type();
}

// ============================================================================
// Smooth Scrolling for Navigation Links
// ============================================================================

/**
 * Handles smooth scrolling when navigation links are clicked
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                // Close mobile menu if open
                closeNavigation();
                
                // Scroll to target with smooth animation
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update active nav link
                updateActiveNav();
            }
        });
    });
}

// ============================================================================
// Active Navigation Link Tracking
// ============================================================================

/**
 * Updates the active navigation link based on scroll position
 */
function updateActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Find which section is currently in view
    let currentSection = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        
        if (window.scrollY >= sectionTop - 200) {
            currentSection = section.getAttribute('id');
        }
    });
    
    // Update active state on nav links
    navLinks.forEach(link => {
        link.classList.remove('active');
        
        const linkHref = link.getAttribute('href').substring(1);
        if (linkHref === currentSection) {
            link.classList.add('active');
        }
    });
}

// ============================================================================
// Mobile Navigation Toggle
// ============================================================================

/**
 * Handles hamburger menu toggle for mobile devices
 */
function initMobileNav() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
}

/**
 * Closes the mobile navigation menu
 */
function closeNavigation() {
    const navLinks = document.querySelector('.nav-links');
    if (navLinks) {
        navLinks.classList.remove('active');
    }
}

// ============================================================================
// Contact Form Handling
// ============================================================================

/**
 * Handles contact form submission via AJAX
 * Sends form data to the server without page reload
 */
function initContactForm() {
    const form = document.getElementById('contactForm');
    
    if (!form) return;
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Show loading state
        const submitBtn = form.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;
        
        try {
            // Collect form data
            const formData = {
                name: document.getElementById('name').value.trim(),
                email: document.getElementById('email').value.trim(),
                subject: document.getElementById('subject').value.trim(),
                message: document.getElementById('message').value.trim(),
            };
            
            // Send data to server
            const response = await fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify(formData)
            });
            
            // Parse response
            const data = await response.json();
            
            // Show result message
            const messageDiv = document.getElementById('formMessage');
            messageDiv.textContent = data.message;
            
            if (data.success) {
                messageDiv.className = 'form-message success';
                form.reset(); // Clear form fields
            } else {
                messageDiv.className = 'form-message error';
            }
            
        } catch (error) {
            // Show error message
            const messageDiv = document.getElementById('formMessage');
            messageDiv.textContent = 'An error occurred. Please try again.';
            messageDiv.className = 'form-message error';
            console.error('Error:', error);
            
        } finally {
            // Restore button state
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

/**
 * Extracts CSRF token from Django templates
 * Required for POST requests in Django
 */
function getCSRFToken() {
    const name = 'csrftoken';
    let cookieValue = null;
    
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    
    return cookieValue;
}

// ============================================================================
// Scroll Animation - Fade In on Scroll
// ============================================================================

/**
 * Animates elements as they enter the viewport
 * Uses Intersection Observer API for performance
 */
function initScrollAnimations() {
    // Elements to animate
    const elementsToAnimate = document.querySelectorAll(
        '.project-card, .skill-item, .timeline-item, .info-item'
    );
    
    if (!elementsToAnimate.length) return;
    
    // Create intersection observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add animation class when element becomes visible
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // Observe all elements
    elementsToAnimate.forEach(element => {
        // Set initial state
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        
        observer.observe(element);
    });
}

// ============================================================================
// Parallax Effect on Scroll
// ============================================================================

/**
 * Creates a subtle parallax effect for the hero section
 */
function initParallax() {
    const hero = document.querySelector('.hero');
    
    if (!hero) return;
    
    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY;
        hero.style.backgroundPosition = `0 ${scrollPosition * 0.5}px`;
    });
}

// ============================================================================
// Highlight Active Section
// ============================================================================

/**
 * Updates highlighting as user scrolls through sections
 */
window.addEventListener('scroll', () => {
    updateActiveNav();
});

// ============================================================================
// Initialize All Scripts on Document Ready
// ============================================================================

/**
 * Runs all initialization functions when DOM is fully loaded
 */
document.addEventListener('DOMContentLoaded', () => {
    console.log('Digital Identity Hub - Initializing...');
    
    // Run all initialization functions
    initTypingEffect();
    initSmoothScroll();
    initMobileNav();
    initContactForm();
    initScrollAnimations();
    initParallax();
    updateActiveNav();
    
    console.log('All scripts initialized successfully!');
});

// ============================================================================
// Utility Functions
// ============================================================================

/**
 * Debounce function - prevents rapid function calls
 * Useful for scroll events and window resize
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle function - limits function calls over time
 * Useful for performance-intensive operations
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ============================================================================
// Console Message
// ============================================================================

console.log('Digital Identity Hub - Frontend loaded successfully!');
console.log('Thank you for visiting!');
