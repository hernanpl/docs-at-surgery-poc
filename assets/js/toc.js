(function() {
  'use strict';
  
  function initTOC() {
    console.log('TOC: initTOC started');
    
    // Only generate TOC on content pages (not home page)
    var pathname = window.location.pathname;
    if (pathname === '/' || pathname === '/index.html' || 
        pathname === '/docs-at-surgery-poc/' || pathname === '/docs-at-surgery-poc/index.html') {
      console.log('TOC: Skipping - home page:', pathname);
      return;
    }
    
    // Find the main content area
    var content = document.querySelector('#main-content') || 
                  document.querySelector('.main-content') || 
                  document.querySelector('main') || 
                  document.querySelector('article') || 
                  document.querySelector('[role="main"]');
    
    console.log('TOC: content element found:', content);
    if (!content) {
      console.log('TOC: No content element found, exiting');
      return;
    }
    
    // Find headings (h2-h6, skip h1 as it's usually the page title)
    var headings = content.querySelectorAll('h2, h3, h4, h5, h6');
    console.log('TOC: headings found:', headings.length);
    if (headings.length === 0) {
      console.log('TOC: No headings found, exiting');
      return;
    }
    
    // Create TOC container
    var tocContainer = document.createElement('div');
    tocContainer.className = 'toc-container';
    
    var tocTitle = document.createElement('a');
    tocTitle.className = 'toc-title';
    tocTitle.href = '#';
    tocTitle.style.textDecoration = 'none';
    tocTitle.style.color = 'inherit';
    
    // Use the page title (from h1, document title, or fallback to "Contents")
    var pageTitle = '';
    var h1 = document.querySelector('h1');
    if (h1) {
      pageTitle = h1.textContent;
    } else if (document.title && document.title !== 'Sonatype Help') {
      pageTitle = document.title.replace(' | Sonatype Help', '');
    } else {
      pageTitle = 'Contents';
    }
    
    tocTitle.textContent = pageTitle;
    
    // Add click handler to scroll to top
    tocTitle.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
    var tocNav = document.createElement('nav');
    tocNav.className = 'toc-nav';
    
    var tocList = document.createElement('ul');
    tocList.className = 'toc-list';
    
    // Build TOC list
    for (var i = 0; i < headings.length; i++) {
      var heading = headings[i];
      
      // Create ID for heading if it doesn't exist
      if (!heading.id) {
        heading.id = 'heading-' + i;
      }
      
      // Create list item
      var listItem = document.createElement('li');
      listItem.className = 'toc-item toc-level-' + heading.tagName.toLowerCase();
      
      var link = document.createElement('a');
      link.href = '#' + heading.id;
      link.textContent = heading.textContent;
      link.className = 'toc-link';
      
      listItem.appendChild(link);
      tocList.appendChild(listItem);
    }
    
    tocNav.appendChild(tocList);
    tocContainer.appendChild(tocTitle);
    tocContainer.appendChild(tocNav);
    
    // Add to page
    console.log('TOC: Adding TOC container to document body');
    document.body.appendChild(tocContainer);
    console.log('TOC: TOC container added successfully');
    
    // Add smooth scrolling
    tocContainer.addEventListener('click', function(e) {
      if (e.target.classList.contains('toc-link')) {
        e.preventDefault();
        var targetId = e.target.getAttribute('href').substring(1);
        var targetElement = document.getElementById(targetId);
        if (targetElement) {
          targetElement.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
    
    // Add scroll spy functionality
    var tocLinks = tocContainer.querySelectorAll('.toc-link');
    var headingsArray = Array.prototype.slice.call(headings);
    
    function updateActiveSection() {
      var scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
      var currentSection = null;
      
      // Find the current section based on scroll position
      for (var i = headingsArray.length - 1; i >= 0; i--) {
        var heading = headingsArray[i];
        var headingTop = heading.offsetTop - 100; // Offset for better UX
        
        if (scrollPosition >= headingTop) {
          currentSection = heading.id;
          break;
        }
      }
      
      // Update active states
      for (var j = 0; j < tocLinks.length; j++) {
        var link = tocLinks[j];
        var linkTarget = link.getAttribute('href').substring(1);
        
        if (linkTarget === currentSection) {
          link.classList.add('active');
        } else {
          link.classList.remove('active');
        }
      }
    }
    
    // Listen for scroll events
    var throttleTimer = null;
    window.addEventListener('scroll', function() {
      if (throttleTimer) {
        clearTimeout(throttleTimer);
      }
      throttleTimer = setTimeout(updateActiveSection, 50);
    });
    
    // Initial call to set active state
    updateActiveSection();
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTOC);
  } else {
    initTOC();
  }
})();