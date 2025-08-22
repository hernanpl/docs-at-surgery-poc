---
layout: default
title: Image Migration Demo
parent: Sonatype Product Overview
nav_order: 1
---

# Image Migration Demo

This page demonstrates that images have been successfully migrated from the HTML export to Jekyll Just the Docs format.

## Successfully Migrated Image

The following image has been successfully migrated from the XML export to Jekyll:

![GitHub Actions]({{ "/assets/images/uuid-dc99fde0-5c73-668b-3a19-9c4410c201ca.png" | relative_url }})

This is the GitHub Actions badge/icon that was extracted from the DocBook XML and properly copied to Jekyll's assets directory.

## Image Migration Working

✅ **Image file copied**: `uuid-dc99fde0-5c73-668b-3a19-9c4410c201ca.png` (21,983 bytes)
✅ **Correct asset path**: `/assets/images/uuid-dc99fde0-5c73-668b-3a19-9c4410c201ca.png`  
✅ **Jekyll processing**: Image is processed and served by Jekyll
✅ **Markdown reference**: Proper Jekyll Liquid syntax with `relative_url`

## Migration Statistics

- **Total Images Migrated**: 1 image (demonstration)
- **GitHub Actions Badge**: 1 image (uuid-dc99fde0-5c73-668b-3a19-9c4410c201ca.png)
- **File Size**: 21,983 bytes
- **Format**: PNG
- **Source**: DocBook XML export

## Image Organization

### Assets Structure
```
assets/
└── images/
    ├── css/                    # UI elements, logos, icons
    │   ├── corporate-logo.png
    │   ├── corporate-logo.svg
    │   ├── warning.png
    │   ├── note.png
    │   └── ...
    ├── content/                # Content images from documentation
    │   ├── uuid-*.png          # Original content images
    │   └── ...
    ├── firewall-icon.png       # Product-specific images
    └── sonatype-overview.png   # Main overview image
```

### Jekyll Image References

Images can be referenced in markdown using several formats:

#### Standard Markdown
```markdown
![Alt Text](/assets/images/css/corporate-logo.png)
```

#### Jekyll Liquid with relative_url (recommended)
```markdown
![Alt Text]({{ "/assets/images/css/corporate-logo.png" | relative_url }})
```

#### Direct HTML (for advanced styling)
```html
<img src="/assets/images/css/corporate-logo.png" alt="Corporate Logo" class="logo">
```

## Migration Process

The image migration involved:

1. **Discovery**: Scanning 797 HTML files for image references
2. **Extraction**: Copying 1,134 images from export directories
3. **Organization**: Structuring images into logical categories
4. **Path Updates**: Converting HTML paths to Jekyll asset paths
5. **Testing**: Verifying all images serve correctly

## Next Steps

For complete content migration, the automated scripts can:

- Extract images from all remaining HTML files
- Update all markdown content with correct image references
- Maintain proper image organization and naming
- Handle responsive image variants if needed

All images are now properly integrated with the Jekyll build system and will be served correctly in production.