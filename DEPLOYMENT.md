# 🚀 Deployment Guide - STC DataHub

Complete guide for deploying STC DataHub to production.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Deployment Options](#deployment-options)
- [Vercel Deployment](#vercel-deployment)
- [SpacetimeDB Setup](#spacetimedb-setup)
- [Environment Variables](#environment-variables)
- [Custom Domain](#custom-domain)
- [Monitoring](#monitoring)
- [Troubleshooting](#troubleshooting)

---

## Overview

STC DataHub can be deployed to various platforms. This guide focuses on:
- **Vercel** (recommended for Next.js)
- **SpacetimeDB Cloud** (for real-time collaboration)

---

## Prerequisites

- ✅ GitHub account
- ✅ Vercel account (free tier available)
- ✅ SpacetimeDB Cloud account (optional, for collaboration)
- ✅ Custom domain (optional)

---

## Deployment Options

### Option 1: Vercel + SpacetimeDB Cloud (Recommended)
- Full feature support
- Real-time collaboration enabled
- Automatic deployments from Git
- Global CDN

### Option 2: Vercel Only
- Basic features work
- No real-time collaboration
- Simpler setup
- Still fully functional for data processing

### Option 3: Self-hosted
- Full control
- Requires server management
- Docker support available

---

## Vercel Deployment

### Quick Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/stc-datahub)

### Manual Deployment

#### 1. Push to GitHub

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Add remote and push
git remote add origin https://github.com/yourusername/stc-datahub.git
git branch -M main
git push -u origin main
```

#### 2. Import to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure project:
   - **Framework Preset**: Next.js
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
   - **Install Command**: `npm install`

#### 3. Deploy

Click "Deploy" - Vercel will automatically build and deploy your app.

### Deployment Configuration

Create `vercel.json` in your project root:

```json
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "regions": ["sin1", "sfo1"],
  "env": {
    "NEXT_PUBLIC_APP_URL": "https://your-domain.com"
  }
}
```

---

## SpacetimeDB Setup

### Option A: SpacetimeDB Cloud (Easiest)

#### 1. Sign Up

Visit [spacetimedb.com](https://spacetimedb.com) and create account.

#### 2. Create Database

```bash
# Install SpacetimeDB CLI
curl --proto '=https' --tlsv1.2 -sSf https://install.spacetimedb.com | sh

# Login
spacetime login

# Publish module to cloud
cd spacetime-server
spacetime publish stc-datahub --clear-database
```

#### 3. Get Connection URL

After publishing, you'll receive a connection URL:
```
wss://your-database.spacetimedb.com
```

#### 4. Update Next.js Environment

Add to Vercel environment variables:

```env
NEXT_PUBLIC_SPACETIME_URL=wss://your-database.spacetimedb.com
NEXT_PUBLIC_SPACETIME_MODULE=stc-datahub
```

### Option B: Self-hosted SpacetimeDB

#### 1. Install SpacetimeDB Server

```bash
# Install server components
curl --proto '=https' --tlsv1.2 -sSf https://install.spacetimedb.com | sh
```

#### 2. Run Server

```bash
# Start server
spacetime start --listen-addr 0.0.0.0:3000

# Publish module
cd spacetime-server
spacetime publish stc-datahub --server http://localhost:3000
```

#### 3. Configure Reverse Proxy (Nginx)

```nginx
server {
    listen 443 ssl;
    server_name spacetime.yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

#### 4. Update Environment

```env
NEXT_PUBLIC_SPACETIME_URL=wss://spacetime.yourdomain.com
NEXT_PUBLIC_SPACETIME_MODULE=stc-datahub
```

---

## Environment Variables

### Required Variables

```env
# App Configuration
NEXT_PUBLIC_APP_URL=https://your-domain.com
NEXT_PUBLIC_APP_NAME=STC DataHub

# SpacetimeDB (optional, for collaboration)
NEXT_PUBLIC_SPACETIME_URL=wss://your-database.spacetimedb.com
NEXT_PUBLIC_SPACETIME_MODULE=stc-datahub
```

### Optional Variables

```env
# Analytics (if using)
NEXT_PUBLIC_GA_ID=G-XXXXXXXXXX

# Feature Flags
NEXT_PUBLIC_ENABLE_COLLABORATION=true
NEXT_PUBLIC_ENABLE_AI_INSIGHTS=true

# API Configuration
NEXT_PUBLIC_API_TIMEOUT=30000
NEXT_PUBLIC_MAX_EXPORT_RECORDS=10000
```

### Setting Environment Variables in Vercel

1. Go to your project in Vercel
2. Navigate to "Settings" → "Environment Variables"
3. Add each variable:
   - **Key**: Variable name (e.g., `NEXT_PUBLIC_SPACETIME_URL`)
   - **Value**: Variable value
   - **Environment**: Select Production, Preview, Development

---

## Custom Domain

### 1. Add Domain in Vercel

1. Go to project "Settings" → "Domains"
2. Add your domain (e.g., `stcdatahub.com`)
3. Vercel will provide DNS records

### 2. Configure DNS

Add these records to your domain registrar:

**For apex domain (stcdatahub.com):**
```
Type: A
Name: @
Value: 76.76.21.21
```

**For www subdomain:**
```
Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

### 3. Verify Domain

Wait for DNS propagation (5-30 minutes), then click "Verify" in Vercel.

### 4. Enable HTTPS

Vercel automatically provisions SSL certificates. Your site will be available via HTTPS.

---

## Monitoring

### Vercel Analytics

Enable in Vercel dashboard:
1. Go to "Analytics" tab
2. Enable Web Analytics
3. View real-time traffic, performance, and errors

### Custom Monitoring

Add monitoring tools:

```typescript
// src/lib/monitoring.ts
export function trackEvent(eventName: string, properties?: Record<string, any>): void {
  // Google Analytics
  if (typeof window !== 'undefined' && window.gtag) {
    window.gtag('event', eventName, properties);
  }
  
  // Custom analytics
  fetch('/api/analytics', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ event: eventName, properties }),
  }).catch(() => {});
}
```

### Error Tracking

Consider integrating:
- **Sentry** - Error tracking
- **LogRocket** - Session replay
- **Datadog** - Full-stack monitoring

---

## Performance Optimization

### 1. Enable Edge Functions

```typescript
// src/app/api/data-share/route.ts
export const runtime = 'edge';
```

### 2. Configure Caching

```typescript
// next.config.js
module.exports = {
  async headers() {
    return [
      {
        source: '/api/:path*',
        headers: [
          {
            key: 'Cache-Control',
            value: 'public, s-maxage=60, stale-while-revalidate=300',
          },
        ],
      },
    ];
  },
};
```

### 3. Image Optimization

Images are automatically optimized by Next.js. Ensure you use the `next/image` component:

```typescript
import Image from 'next/image';

<Image 
  src="/logo.png" 
  alt="Logo" 
  width={200} 
  height={50}
  priority
/>
```

---

## Troubleshooting

### Build Failures

**Issue**: Build fails with TypeScript errors

```bash
# Fix locally
npm run build

# Check for type errors
npx tsc --noEmit
```

**Issue**: Out of memory during build

Add to `vercel.json`:
```json
{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/next",
      "config": { "maxLambdaSize": "50mb" }
    }
  ]
}
```

### SpacetimeDB Connection Issues

**Issue**: Cannot connect to SpacetimeDB

1. Check environment variables in Vercel
2. Verify SpacetimeDB module is published
3. Check browser console for WebSocket errors
4. Ensure CORS is properly configured

**Issue**: "Module not found" error

```bash
# Re-publish module
cd spacetime-server
spacetime publish stc-datahub --clear-database --force
```

### API Errors

**Issue**: CORS errors in production

Add CORS headers to API routes:

```typescript
export async function GET(request: Request): Promise<Response> {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };
  
  // ... your logic
  
  return new Response(JSON.stringify(data), { headers });
}
```

### Performance Issues

**Issue**: Slow page loads

1. Check Vercel Analytics for bottlenecks
2. Enable ISR (Incremental Static Regeneration)
3. Optimize images and assets
4. Use Edge Functions for API routes
5. Implement proper caching strategies

---

## Rollback Strategy

### Vercel Rollback

1. Go to "Deployments" in Vercel dashboard
2. Find previous working deployment
3. Click "..." menu → "Promote to Production"

### SpacetimeDB Rollback

```bash
# Republish previous version
cd spacetime-server
git checkout <previous-commit>
spacetime publish stc-datahub --force
```

---

## Backup Strategy

### Database Backups

```bash
# Export SpacetimeDB data
spacetime call stc-datahub export_all_data > backup.json

# Restore from backup
spacetime call stc-datahub import_data --data backup.json
```

### Code Backups

- Use Git tags for releases
- Keep production branch protected
- Maintain staging environment

---

## CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Node
        uses: actions/setup-node@v2
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm install
      
      - name: Build
        run: npm run build
      
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

---

## Post-Deployment Checklist

- [ ] Verify all pages load correctly
- [ ] Test real-time collaboration (if enabled)
- [ ] Check API endpoints are responding
- [ ] Verify data export functionality
- [ ] Test mobile responsiveness
- [ ] Check language switcher (EN/ID)
- [ ] Verify custom domain works
- [ ] Ensure HTTPS is enabled
- [ ] Test error pages (404, 500)
- [ ] Monitor initial traffic for errors

---

## Support

For deployment issues:
- **Vercel Support**: [vercel.com/support](https://vercel.com/support)
- **SpacetimeDB Docs**: [docs.spacetimedb.com](https://docs.spacetimedb.com)
- **Project Issues**: [GitHub Issues](https://github.com/yourusername/stc-datahub/issues)

---

**Congratulations! Your STC DataHub is now live! 🎉**
