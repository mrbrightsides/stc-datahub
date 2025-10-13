# 🔗 API Documentation - STC DataHub

Complete API reference for STC DataHub REST endpoints.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Base URL](#base-url)
- [Endpoints](#endpoints)
  - [GET /api/data-share](#get-apidata-share)
  - [GET /api/stats](#get-apistats)
- [Response Formats](#response-formats)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)
- [Examples](#examples)

---

## Overview

STC DataHub provides RESTful API endpoints for accessing normalized tourism data. All endpoints return JSON and support CORS for cross-origin requests.

### Features

- ✅ Public access (no authentication required for read operations)
- ✅ CORS enabled for external integrations
- ✅ Pagination support
- ✅ Advanced filtering
- ✅ Consistent error handling
- ✅ JSON response format

---

## Authentication

Currently, all read endpoints are **public** and require no authentication. Future versions will support API keys for write operations.

---

## Base URL

```
Development: http://localhost:3000
Production: https://your-domain.com
```

---

## Endpoints

### GET `/api/data-share`

Fetch tourism data with filtering and pagination support.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | number | No | Page number (default: 1) |
| `limit` | number | No | Items per page (default: 50, max: 100) |
| `category` | string | No | Filter by category (hotel, restaurant, attraction, etc.) |
| `country` | string | No | Filter by country name |
| `minRating` | number | No | Minimum rating (0-5) |
| `source` | string | No | Filter by data source |

#### Response

```json
{
  "success": true,
  "data": [
    {
      "id": "uuid-here",
      "name": "Grand Hotel Jakarta",
      "description": "Luxury hotel in central Jakarta",
      "category": "hotel",
      "location": {
        "country": "Indonesia",
        "city": "Jakarta",
        "address": "Jl. Sudirman No. 1",
        "coordinates": {
          "latitude": -6.2088,
          "longitude": 106.8456
        }
      },
      "contact": {
        "phone": "+62-21-12345678",
        "email": "info@grandhotel.com",
        "website": "https://grandhotel.com"
      },
      "rating": 4.5,
      "reviewCount": 1250,
      "priceRange": "$$$",
      "features": ["wifi", "pool", "spa"],
      "images": ["url1.jpg", "url2.jpg"],
      "dataSource": "manual",
      "lastUpdated": "2024-01-15T10:30:00Z",
      "status": "active"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 50,
    "total": 500,
    "totalPages": 10,
    "hasNext": true,
    "hasPrev": false
  },
  "filters": {
    "category": "hotel",
    "country": "Indonesia",
    "minRating": 4.0
  }
}
```

#### Example Requests

```bash
# Get all data (paginated)
curl "http://localhost:3000/api/data-share"

# Filter by category
curl "http://localhost:3000/api/data-share?category=hotel"

# Filter by country and rating
curl "http://localhost:3000/api/data-share?country=Indonesia&minRating=4.0"

# Pagination with filters
curl "http://localhost:3000/api/data-share?page=2&limit=20&category=restaurant"

# Multiple filters
curl "http://localhost:3000/api/data-share?category=attraction&country=Thailand&minRating=4.5&limit=10"
```

#### Status Codes

- `200 OK` - Success
- `400 Bad Request` - Invalid parameters
- `500 Internal Server Error` - Server error

---

### GET `/api/stats`

Get aggregated statistics about tourism data.

#### Parameters

None

#### Response

```json
{
  "success": true,
  "stats": {
    "overview": {
      "totalRecords": 5000,
      "totalCountries": 150,
      "totalCategories": 8,
      "averageRating": 4.2,
      "lastUpdated": "2024-01-15T10:30:00Z"
    },
    "byCategory": {
      "hotel": 1200,
      "restaurant": 1500,
      "attraction": 1000,
      "museum": 500,
      "park": 400,
      "beach": 300,
      "shopping": 80,
      "other": 20
    },
    "byCountry": {
      "Indonesia": 1500,
      "Thailand": 1200,
      "Singapore": 800,
      "Malaysia": 700,
      "Philippines": 500
    },
    "topCountries": [
      {
        "country": "Indonesia",
        "count": 1500,
        "averageRating": 4.3
      },
      {
        "country": "Thailand",
        "count": 1200,
        "averageRating": 4.5
      }
    ],
    "ratingDistribution": {
      "5": 1000,
      "4": 2000,
      "3": 1500,
      "2": 400,
      "1": 100
    },
    "dataQuality": {
      "withCoordinates": 4500,
      "withImages": 3800,
      "withContact": 4200,
      "completeness": 85.5
    }
  }
}
```

#### Example Request

```bash
curl "http://localhost:3000/api/stats"
```

#### Status Codes

- `200 OK` - Success
- `500 Internal Server Error` - Server error

---

## Response Formats

All API responses follow a consistent structure:

### Success Response

```json
{
  "success": true,
  "data": [...],
  "pagination": {...},
  "meta": {...}
}
```

### Error Response

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid parameter: limit must be between 1 and 100",
    "details": {
      "parameter": "limit",
      "value": 150,
      "constraint": "max: 100"
    }
  }
}
```

---

## Error Handling

### Common Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Invalid request parameters |
| `NOT_FOUND` | Resource not found |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INTERNAL_ERROR` | Server error |

### HTTP Status Codes

- `200 OK` - Request successful
- `400 Bad Request` - Invalid parameters
- `404 Not Found` - Endpoint not found
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error
- `503 Service Unavailable` - Service temporarily unavailable

---

## Rate Limiting

Currently no rate limiting is enforced, but future versions will implement:

- **Anonymous**: 100 requests/minute
- **Authenticated**: 1000 requests/minute
- **Premium**: Unlimited

Rate limit headers will be included in responses:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
```

---

## Examples

### JavaScript/TypeScript

```typescript
// Fetch data with filters
const response = await fetch(
  'http://localhost:3000/api/data-share?category=hotel&country=Indonesia&limit=10'
);
const data = await response.json();

if (data.success) {
  console.log(`Found ${data.data.length} hotels`);
  data.data.forEach(hotel => {
    console.log(`${hotel.name} - Rating: ${hotel.rating}`);
  });
}

// Get statistics
const statsResponse = await fetch('http://localhost:3000/api/stats');
const stats = await statsResponse.json();

if (stats.success) {
  console.log(`Total records: ${stats.stats.overview.totalRecords}`);
  console.log(`Average rating: ${stats.stats.overview.averageRating}`);
}
```

### Python

```python
import requests

# Fetch data
response = requests.get(
    'http://localhost:3000/api/data-share',
    params={
        'category': 'hotel',
        'country': 'Indonesia',
        'minRating': 4.0,
        'limit': 10
    }
)

data = response.json()

if data['success']:
    print(f"Found {len(data['data'])} hotels")
    for hotel in data['data']:
        print(f"{hotel['name']} - {hotel['rating']} stars")

# Get statistics
stats_response = requests.get('http://localhost:3000/api/stats')
stats = stats_response.json()

if stats['success']:
    print(f"Total: {stats['stats']['overview']['totalRecords']}")
```

### cURL

```bash
# Basic request
curl "http://localhost:3000/api/data-share"

# With filters
curl "http://localhost:3000/api/data-share?category=restaurant&country=Thailand&minRating=4.5"

# Get stats
curl "http://localhost:3000/api/stats"

# Pretty print JSON
curl "http://localhost:3000/api/stats" | jq '.'
```

---

## CORS Support

All endpoints support CORS with the following headers:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

This allows external websites and applications to consume the API directly from the browser.

---

## Webhooks (Coming Soon)

Future versions will support webhooks for real-time notifications:

- New data added
- Data updated
- Processing completed
- Quality alerts

---

## GraphQL API (Planned)

A GraphQL endpoint is planned for more flexible data queries:

```graphql
query {
  tourism(
    filters: {
      category: "hotel"
      country: "Indonesia"
      minRating: 4.0
    }
    pagination: {
      page: 1
      limit: 10
    }
  ) {
    data {
      id
      name
      rating
      location {
        country
        city
        coordinates {
          latitude
          longitude
        }
      }
    }
    pagination {
      total
      hasNext
    }
  }
}
```

---

## Support

For API support:
- **Documentation Issues**: Open GitHub issue
- **Integration Help**: discussions@stcdatahub.com
- **Bug Reports**: bugs@stcdatahub.com

---

**Last Updated**: January 2024  
**API Version**: 1.0.0
