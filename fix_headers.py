#!/usr/bin/env python3
import os
import re

# The correct header content from index.html
new_header = '''    <div class="vs-header__top">
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

# Get all HTML files except index.html and 404.html
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['index.html', '404.html']]

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Multiple patterns to catch different header formats
        patterns = [
            r'<div class="vs-header__top">.*?</div>\s*</div>\s*</div>',
            r'<!-- Header Top -->.*?<div class="vs-header__top">.*?</div>\s*</div>\s*</div>',
            r'<div class="vs-header__top">[\s\S]*?<div class="social-style">[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*</div>'
        ]
        
        updated = False
        for pattern in patterns:
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, new_header, content, flags=re.DOTALL)
                updated = True
                break
        
        if updated:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✓ Updated {filename}')
        else:
            print(f'✗ No header pattern found in {filename}')
            
    except Exception as e:
        print(f'Error processing {filename}: {e}')

print('Header update process completed!')
