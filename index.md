---
layout: home
title: Home
nav_exclude: true
---

<div class="welcome-section">
  <h1>Welcome to the Sonatype Help Center</h1>
  <p class="welcome-subtitle">Whether you're setting up, scaling up, or just need a quick answer, we've got you covered.</p>
</div>

<div class="product-cards">
  <a href="/docs/sonatype-product-overview/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-product-overview.png" alt="Sonatype Product Overview">
    </div>
    <h3>Sonatype Product Overview</h3>
    <p>Important announcements, sunsetting information, and solution overview.</p>
  </a>

  <a href="/docs/sonatype-nexus-repository/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-nexus-repository.png" alt="Sonatype Nexus Repository">
    </div>
    <h3>Sonatype Nexus Repository</h3>
    <p>Store, organize, and share software components securely and efficiently.</p>
  </a>

  <a href="/docs/sonatype-iq-server/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-iq-server.png" alt="Sonatype IQ Server">
    </div>
    <h3>Sonatype IQ Server</h3>
    <p>Downloads and system requirements for the server that powers Lifecycle, Developer, SBOM Manager, and Firewall.</p>
  </a>

  <a href="/docs/sonatype-lifecycle/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-lifecycle.png" alt="Sonatype Lifecycle">
    </div>
    <h3>Sonatype Lifecycle</h3>
    <p>Policy enforcement throughout the software development lifecycle.</p>
  </a>

  <a href="/docs/sonatype-repository-firewall/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-repository-firewall.png" alt="Sonatype Repository Firewall">
    </div>
    <h3>Sonatype Repository Firewall</h3>
    <p>Block malicious components before they enter your software supply chain.</p>
  </a>

  <a href="/docs/sonatype-sbom-manager/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-sbom-manager.png" alt="Sonatype SBOM Manager">
    </div>
    <h3>Sonatype SBOM Manager</h3>
    <p>Ensure adherence with automated software bill of materials generation and reporting.</p>
  </a>

  <a href="/docs/sonatype-developer/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-developer.png" alt="Sonatype Developer">
    </div>
    <h3>Sonatype Developer</h3>
    <p>Developer-centric tools for managing open-source component quality.</p>
  </a>

  <a href="/docs/sonatype-integrations/" class="product-card">
    <div class="card-icon">
      <img src="/assets/images/logo-integrations.png" alt="Sonatype Integrations">
    </div>
    <h3>Sonatype Integrations</h3>
    <p>CI/CD, SCM, and IDE plugins for Sonatype solutions.</p>
  </a>
</div>

<style>
.welcome-section {
  text-align: center;
  margin: 2rem 0 3rem 0;
  padding: 2rem 0;
}

.welcome-section h1 {
  font-size: 2.5rem;
  color: #27262b;
  margin-bottom: 1rem;
  font-weight: 600;
}

.welcome-subtitle {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 0;
  max-width: 600px;
  margin: 0 auto;
}

.product-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
  padding: 0 1rem;
}

.product-card {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  color: inherit;
  display: block;
}

.product-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border-color: #5755d9;
  text-decoration: none;
  color: inherit;
}

.card-icon {
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
}

.card-icon img {
  max-width: 60px;
  max-height: 60px;
  width: auto;
  height: auto;
}

.product-card h3 {
  font-size: 1.3rem;
  margin: 0 0 0.75rem 0;
  color: #27262b;
}

.product-card:hover h3 {
  color: #5755d9;
}

.product-card p {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 768px) {
  .welcome-section h1 {
    font-size: 2rem;
  }
  
  .welcome-subtitle {
    font-size: 1.1rem;
  }
  
  .product-cards {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0 0.5rem;
  }
  
  .product-card {
    padding: 1.25rem;
  }
}
</style>