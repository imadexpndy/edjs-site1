#!/usr/bin/env python3
import os
import re

# The new header content from index.html
new_header_content = '''    <div class="vs-header__top">
      <div class="container container--custom">
        <div class="row align-items-center justify-content-between gy-1 text-center text-lg-start">
          <div class="col-lg-auto d-none d-lg-block">
            <div class="d-flex align-items-center flex-wrap gap-4">
              <div class="vs-header__info">
                <i class="fa-solid fa-envelope"></i>
                <span> Email : <a href="mailto:info@edjs.ma">info@edjs.ma</a></span>
              </div>
              <div class="vs-header__info">
                <i class="fa-solid fa-phone-volume"></i>
                <span> Téléphone : <a href="tel:+212522981085">+212 5 22 98 10 85</a></span>
              </div>
            </div>
          </div>
          <div class="col-lg-auto">
            <div class="social-style">
              <span class="social-style__label">suivez-nous :</span>
              <a href="#"><i class="fab fa-facebook-f"></i></a>
              <a href="#"><i class="fab fa-linkedin-in"></i></a>
              <a href="#"><i class="fab fa-youtube"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>'''

# List of HTML files to update (excluding index.html and assets folder)
html_files = [
    'contact.html', 'spectacles.html', 'gallery.html', 'blog.html', 'blog-details.html',
    'registration.html', 'partners.html', 'spectacle-charlotte.html', 'spectacle-casse-noisette.html',
    'spectacle-le-petit-prince.html', 'spectacle-leau-la.html', 'spectacle-tara-sur-la-lune.html',
    'spectacle-simple-comme-bonjour.html', 'spectacle-estevanico.html', 'spectacle-lenfant-de-larbre.html',
    'spectacle-antigone.html', 'spectacle-alice-chez-les-merveilles.html'
]

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Pattern to match the vs-header__top section
        pattern = r'<div class="vs-header__top">.*?</div>\s*</div>\s*</div>'
        
        # Replace the header content
        updated_content = re.sub(pattern, new_header_content, content, flags=re.DOTALL)
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"Updated {filename}")

print("Header update complete!")
