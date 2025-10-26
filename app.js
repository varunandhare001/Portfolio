// Global state
let currentCarouselIndex = 0;
let isScrolling = false;

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    initLoadingScreen();
    initCustomCursor();
    initScrollProgress();
    initNavigation();
    initScrollAnimations();
    initAccordion();
    initVideoCards();
    initCarousel();
    initCertificateCards();
    initProofCards();
    initBackToTop();
    initParticles();
    initCircuitBackground();
    initContactForm();
    initParallax();
});

// Loading Screen
function initLoadingScreen() {
    setTimeout(() => {
        const loadingScreen = document.getElementById('loading-screen');
        loadingScreen.classList.add('hidden');
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 500);
    }, 2000);
}

// Custom Cursor
function initCustomCursor() {
    const cursor = document.getElementById('custom-cursor');
    
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });
    
    // Scale cursor on clickable elements
    const clickables = document.querySelectorAll('a, button, .nav-card, .video-card, .certificate-card, .proof-card');
    clickables.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'scale(2)';
        });
        el.addEventListener('mouseleave', () => {
            cursor.style.transform = 'scale(1)';
        });
    });
}

// Scroll Progress
function initScrollProgress() {
    const progressBar = document.getElementById('scroll-progress');
    
    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    });
}

// Navigation
function initNavigation() {
    // Header hide/show on scroll
    let lastScroll = 0;
    const header = document.getElementById('header');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        
        if (currentScroll > lastScroll && currentScroll > 100) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
    });
    
    // Navigation cards smooth scroll
    const navCards = document.querySelectorAll('.nav-card');
    navCards.forEach(card => {
        card.addEventListener('click', () => {
            const sectionId = card.getAttribute('data-section');
            const section = document.getElementById(sectionId);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    
    // Nav links smooth scroll
    const navLinks = document.querySelectorAll('.nav-link, a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
}

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    // Observe fade-in elements
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(el => observer.observe(el));
}

// Accordion
function initAccordion() {
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const item = header.parentElement;
            const wasActive = item.classList.contains('active');
            
            // Close all accordion items
            document.querySelectorAll('.accordion-item').forEach(accItem => {
                accItem.classList.remove('active');
            });
            
            // Open clicked item if it wasn't active
            if (!wasActive) {
                item.classList.add('active');
            }
        });
    });
}

// Video Cards and Modal
function initVideoCards() {
    const videoCards = document.querySelectorAll('.video-card');
    const modal = document.getElementById('video-modal');
    const modalVideo = document.getElementById('modal-video');
    const closeBtn = modal.querySelector('.modal-close');
    const overlay = modal.querySelector('.modal-overlay');
    
    videoCards.forEach(card => {
        card.addEventListener('click', () => {
            const videoId = card.getAttribute('data-video');
            modalVideo.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
            modal.classList.add('active');
        });
    });
    
    function closeModal() {
        modal.classList.remove('active');
        modalVideo.src = '';
    }
    
    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', closeModal);
    
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

// Carousel
function initCarousel() {
    const track = document.querySelector('.carousel-track');
    const cards = document.querySelectorAll('.choreo-card');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const dotsContainer = document.querySelector('.carousel-dots');
    
    if (!track || cards.length === 0) return;
    
    // Create dots
    cards.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('carousel-dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
    
    function updateCarousel() {
        const cardWidth = cards[0].offsetWidth;
        const gap = 30;
        track.style.transform = `translateX(-${currentCarouselIndex * (cardWidth + gap)}px)`;
        
        // Update dots
        document.querySelectorAll('.carousel-dot').forEach((dot, index) => {
            dot.classList.toggle('active', index === currentCarouselIndex);
        });
    }
    
    function goToSlide(index) {
        currentCarouselIndex = Math.max(0, Math.min(index, cards.length - 1));
        updateCarousel();
    }
    
    prevBtn.addEventListener('click', () => {
        if (currentCarouselIndex > 0) {
            currentCarouselIndex--;
            updateCarousel();
        }
    });
    
    nextBtn.addEventListener('click', () => {
        if (currentCarouselIndex < cards.length - 1) {
            currentCarouselIndex++;
            updateCarousel();
        }
    });
}

// Certificate Cards
function initCertificateCards() {
    const certCards = document.querySelectorAll('.certificate-card');
    const modal = document.getElementById('cert-modal');
    const closeBtn = modal.querySelector('.modal-close');
    const overlay = modal.querySelector('.modal-overlay');
    const modalTitle = document.getElementById('cert-modal-title');
    const modalDesc = document.getElementById('cert-modal-description');
    
    const certData = {
        'aws': {
            title: 'AWS Certified Solutions Architect',
            description: 'This certification validates expertise in designing distributed systems on AWS.'
        },
        'ccna': {
            title: 'Cisco CCNA',
            description: 'This certification demonstrates knowledge of networking fundamentals and Cisco technologies.'
        },
        'google': {
            title: 'Google IT Support Professional',
            description: 'This certification validates skills in troubleshooting, customer service, networking, and security.'
        }
    };
    
    certCards.forEach(card => {
        card.addEventListener('click', () => {
            const certId = card.getAttribute('data-cert');
            const data = certData[certId];
            
            if (data) {
                modalTitle.textContent = data.title;
                modalDesc.textContent = data.description;
                modal.classList.add('active');
            }
        });
    });
    
    function closeModal() {
        modal.classList.remove('active');
    }
    
    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', closeModal);
    
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

// Proof Cards
function initProofCards() {
    const proofCards = document.querySelectorAll('.proof-card');
    
    proofCards.forEach(card => {
        card.addEventListener('click', () => {
            const lockIcon = card.querySelector('.lock-icon');
            if (lockIcon.textContent === '🔒') {
                lockIcon.textContent = '🔓';
                card.style.background = 'linear-gradient(135deg, rgba(255, 190, 11, 0.2), rgba(58, 134, 255, 0.2))';
            } else {
                lockIcon.textContent = '🔒';
                card.style.background = '';
            }
        });
    });
}

// Back to Top Button
function initBackToTop() {
    const backToTopBtn = document.getElementById('back-to-top');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });
    
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Particles Canvas
function initParticles() {
    const canvas = document.getElementById('particles-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const particleCount = 100;
    
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 1;
            this.speedX = Math.random() * 1 - 0.5;
            this.speedY = Math.random() * 1 - 0.5;
            this.color = ['#ff006e', '#8338ec', '#3a86ff'][Math.floor(Math.random() * 3)];
        }
        
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            
            if (this.x > canvas.width) this.x = 0;
            if (this.x < 0) this.x = canvas.width;
            if (this.y > canvas.height) this.y = 0;
            if (this.y < 0) this.y = canvas.height;
        }
        
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });
        
        // Draw connections
        particles.forEach((a, i) => {
            particles.slice(i + 1).forEach(b => {
                const dx = a.x - b.x;
                const dy = a.y - b.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    ctx.strokeStyle = `rgba(58, 134, 255, ${1 - distance / 100})`;
                    ctx.lineWidth = 0.5;
                    ctx.beginPath();
                    ctx.moveTo(a.x, a.y);
                    ctx.lineTo(b.x, b.y);
                    ctx.stroke();
                }
            });
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
    
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// Circuit Background
function initCircuitBackground() {
    const canvas = document.getElementById('circuit-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.parentElement.offsetWidth;
    canvas.height = canvas.parentElement.offsetHeight;
    
    function drawCircuit() {
        ctx.strokeStyle = '#06ffa5';
        ctx.lineWidth = 2;
        
        // Draw random circuit lines
        for (let i = 0; i < 20; i++) {
            ctx.beginPath();
            const startX = Math.random() * canvas.width;
            const startY = Math.random() * canvas.height;
            ctx.moveTo(startX, startY);
            
            for (let j = 0; j < 5; j++) {
                const endX = startX + (Math.random() - 0.5) * 200;
                const endY = startY + (Math.random() - 0.5) * 200;
                ctx.lineTo(endX, endY);
            }
            
            ctx.stroke();
        }
        
        // Draw circuit nodes
        ctx.fillStyle = '#06ffa5';
        for (let i = 0; i < 30; i++) {
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height;
            ctx.beginPath();
            ctx.arc(x, y, 3, 0, Math.PI * 2);
            ctx.fill();
        }
    }
    
    drawCircuit();
}

// Contact Form
function initContactForm() {
    const form = document.querySelector('.contact-form');
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;
        
        // Here you would normally send the form data to a server
        alert(`Thank you, ${name}! Your message has been received. We'll get back to you at ${email}.`);
        
        form.reset();
    });
}

// Parallax Effect
function initParallax() {
    const parallaxElements = document.querySelectorAll('.nav-card, .project-card, .avatar-container');
    
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        
        parallaxElements.forEach(el => {
            el.style.transform = `translate(${x}px, ${y}px)`;
        });
    });
}

// Download buttons
document.querySelectorAll('.download-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        alert('Download feature will be implemented with actual PDF/file links.');
    });
});