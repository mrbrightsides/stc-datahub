# 🏗️ Architecture Overview - STC DataHub

Technical architecture and design decisions for STC DataHub.

---

## 📋 Table of Contents

- [System Overview](#system-overview)
- [Technology Stack](#technology-stack)
- [Architecture Patterns](#architecture-patterns)
- [Data Flow](#data-flow)
- [Component Architecture](#component-architecture)
- [Database Design](#database-design)
- [API Design](#api-design)
- [Real-time Collaboration](#real-time-collaboration)
- [Security](#security)
- [Performance](#performance)
- [Scalability](#scalability)

---

## System Overview

STC DataHub is a full-stack Next.js application with real-time collaboration capabilities, designed for processing and visualizing tourism data at scale.

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Client (Browser)                      │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────┐  │
│  │  Next.js   │  │   React    │  │   Tailwind CSS   │  │
│  │  App Router│  │ Components │  │    + shadcn/ui   │  │
│  └────────────┘  └────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│                  Next.js API Routes                      │
│  ┌──────────────┐  ┌─────────────┐  ┌───────────────┐  │
│  │ Data Sharing │  │ Statistics  │  │ Proxy (CORS)  │  │
│  │   /api/data  │  │ /api/stats  │  │ /api/proxy    │  │
│  └──────────────┘  └─────────────┘  └───────────────┘  │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│              Data Processing Pipeline                    │
│  Fetch → Validate → Normalize → Enrich → Store          │
└─────────────────────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ External APIs│  │  SpacetimeDB │  │ Local Storage│
│              │  │  (Real-time) │  │  (Browser)   │
│ • REST       │  │              │  │              │
│ • OpenStreet │  │ WebSocket    │  │ IndexedDB    │
│ • Breweries  │  │ Connection   │  │ localStorage │
└──────────────┘  └──────────────┘  └──────────────┘
```

---

## Technology Stack

### Frontend

| Technology | Purpose | Version |
|------------|---------|---------|
| **Next.js** | React framework with SSR/SSG | 15.1.3 |
| **React** | UI library | 19.x |
| **TypeScript** | Type-safe development | 5.x |
| **Tailwind CSS** | Utility-first styling | 3.x |
| **shadcn/ui** | Component library | Latest |

### Data Visualization

| Technology | Purpose |
|------------|---------|
| **Recharts** | Charts and graphs |
| **Leaflet** | Interactive maps |
| **heatmap.js** | Density visualizations |
| **react-grid-layout** | Dashboard builder |

### Backend & Data

| Technology | Purpose |
|------------|---------|
| **SpacetimeDB** | Real-time database & collaboration |
| **Rust** | SpacetimeDB server modules |
| **WebSocket** | Real-time communication |

### Internationalization

| Technology | Purpose |
|------------|---------|
| **i18next** | Multi-language support |
| **react-i18next** | React integration |

---

## Architecture Patterns

### 1. Component-Based Architecture

```
src/components/
├── ui/                    # Reusable UI primitives (shadcn)
│   ├── button.tsx
│   ├── card.tsx
│   └── input.tsx
│
├── dashboard/             # Business logic components
│   ├── connector-card.tsx
│   ├── dataset-preview.tsx
│   └── advanced-filters.tsx
│
├── visualization/         # Data visualization
│   ├── data-charts.tsx
│   ├── interactive-map.tsx
│   └── heatmap-viz.tsx
│
└── collaboration/         # Real-time features
    ├── user-presence.tsx
    └── activity-feed.tsx
```

### 2. Server-Side Rendering (SSR)

- **App Router**: Pages are server-rendered by default
- **Client Components**: Marked with `'use client'` for interactivity
- **API Routes**: Edge functions for optimal performance

### 3. State Management

```typescript
// Local state with React hooks
const [data, setData] = useState<TourismData[]>([]);

// Global state with Context (when needed)
const { language, setLanguage } = useLanguage();

// Real-time state with SpacetimeDB
const users = useSpacetimeQuery('select * from CollabUser');
```

### 4. Data Processing Pipeline

```typescript
interface PipelineStage {
  name: string;
  process: (data: any) => Promise<any>;
  validate: (data: any) => boolean;
}

const pipeline: PipelineStage[] = [
  { name: 'Fetch', process: fetchData, validate: validateFetch },
  { name: 'Validate', process: validateData, validate: validateSchema },
  { name: 'Normalize', process: normalizeData, validate: validateNormalized },
  { name: 'Enrich', process: enrichData, validate: validateEnriched },
  { name: 'Store', process: storeData, validate: validateStored },
];
```

---

## Data Flow

### Data Processing Flow

```
1. User Creates Connector
   ↓
2. Select Data Source (REST Countries, OpenStreetMap, etc.)
   ↓
3. Configure Parameters (limit, location, filters)
   ↓
4. Test Connection
   ↓
5. Start Connector
   ↓
6. Data Processing Pipeline:
   
   Fetch Stage
   ├─ Call external API
   ├─ Handle rate limits
   └─ Return raw data
   
   Validate Stage
   ├─ Check required fields
   ├─ Validate data types
   └─ Flag invalid records
   
   Normalize Stage
   ├─ Map to standard schema
   ├─ Handle missing fields
   └─ Format consistently
   
   Enrich Stage
   ├─ Add metadata
   ├─ Geocode addresses
   └─ Categorize data
   
   Store Stage
   ├─ Save to local state
   ├─ Broadcast to SpacetimeDB
   └─ Update UI
   
   ↓
7. Data Available for:
   - Visualization (charts, maps, heatmaps)
   - Export (7 formats)
   - Analysis (AI insights)
   - Sharing (REST API)
```

### Real-time Collaboration Flow

```
User A                    SpacetimeDB              User B
  │                            │                      │
  ├─ Join Session ────────────>│                      │
  │  (WebSocket connect)       │                      │
  │                            │<──── Join Session ───┤
  │                            │                      │
  ├─ Add Dataset ─────────────>│                      │
  │                            ├─ Broadcast ─────────>│
  │                            │  (new dataset)       │
  │                            │                      │
  │                            │<──── Edit Data ──────┤
  │<──── Broadcast ────────────┤                      │
  │  (data change)             │                      │
  │                            │                      │
  ├─ Export Data ─────────────>│                      │
  │                            ├─ Broadcast ─────────>│
  │                            │  (export action)     │
```

---

## Component Architecture

### Core Components

#### 1. Dashboard Component (`src/app/page.tsx`)

Main application shell with tab navigation.

```typescript
'use client';

export default function DashboardPage(): JSX.Element {
  const [activeTab, setActiveTab] = useState<string>('connectors');
  
  return (
    <div className="dashboard">
      <Tabs value={activeTab} onValueChange={setActiveTab}>
        <TabsList>
          <TabsTrigger value="connectors">Connectors</TabsTrigger>
          <TabsTrigger value="datasets">Datasets</TabsTrigger>
          <TabsTrigger value="analytics">Analytics</TabsTrigger>
          <TabsTrigger value="ai-insights">AI Insights</TabsTrigger>
          <TabsTrigger value="dashboard">Dashboard</TabsTrigger>
          <TabsTrigger value="collaboration">Collaboration</TabsTrigger>
        </TabsList>
        {/* Tab contents */}
      </Tabs>
    </div>
  );
}
```

#### 2. Data Processing (`src/lib/real-data-sources.ts`)

Connector implementations for external APIs.

```typescript
export interface DataSource {
  id: string;
  name: string;
  description: string;
  configurable: boolean;
  fetch: (config: SourceConfig) => Promise<TourismData[]>;
  test: () => Promise<{ success: boolean; message: string }>;
}

export const dataSources: DataSource[] = [
  {
    id: 'rest-countries',
    name: 'REST Countries API',
    fetch: async (config) => {
      const response = await fetch('https://restcountries.com/v3.1/all');
      const countries = await response.json();
      return countries.map(mapCountryToTourismData);
    },
  },
  // More sources...
];
```

#### 3. Visualization (`src/components/visualization/`)

Reusable chart and map components.

```typescript
// Data Charts
export function DataCharts({ data }: { data: TourismData[] }): JSX.Element {
  return (
    <>
      <PieChart data={categoryDistribution(data)} />
      <BarChart data={countryDistribution(data)} />
      <LineChart data={ratingTrends(data)} />
    </>
  );
}

// Interactive Map
export function InteractiveMap({ data }: { data: TourismData[] }): JSX.Element {
  return (
    <MapContainer>
      {data.map(item => (
        <Marker position={item.coordinates} key={item.id}>
          <Popup>{item.name}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}
```

---

## Database Design

### SpacetimeDB Schema

```rust
// spacetime-server/src/lib.rs

#[spacetimedb::table(name = collab_user)]
pub struct CollabUser {
    #[primary_key]
    pub user_id: String,
    pub name: String,
    pub color: String,
    pub last_seen: Timestamp,
    pub status: String, // "online" | "away" | "offline"
}

#[spacetimedb::table(name = collab_session)]
pub struct CollabSession {
    #[primary_key]
    pub session_id: String,
    pub created_at: Timestamp,
    pub active_users: Vec<String>,
}

#[spacetimedb::table(name = data_change)]
pub struct DataChange {
    #[primary_key]
    pub change_id: String,
    pub user_id: String,
    pub action: String, // "add" | "edit" | "delete" | "export"
    pub dataset_id: String,
    pub timestamp: Timestamp,
    pub description: String,
}

// Reducers (database functions)
#[spacetimedb::reducer]
pub fn join_session(ctx: &ReducerContext, user_id: String, name: String) {
    // Add user to session
}

#[spacetimedb::reducer]
pub fn broadcast_change(ctx: &ReducerContext, change: DataChange) {
    // Notify all connected clients
}
```

### Local Storage Schema

```typescript
// Browser localStorage
interface LocalStorageData {
  // Connectors
  connectors: Connector[];
  
  // Datasets
  datasets: Dataset[];
  
  // User preferences
  preferences: {
    language: 'en' | 'id';
    theme: 'light' | 'dark';
    dashboardLayout: GridLayout[];
  };
  
  // Cache
  cache: {
    lastFetch: number;
    data: any;
  };
}
```

---

## API Design

### REST API Endpoints

#### GET `/api/data-share`

```typescript
// Request
GET /api/data-share?category=hotel&country=Indonesia&page=1&limit=10

// Response
{
  "success": true,
  "data": TourismData[],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 500,
    "totalPages": 50
  }
}
```

#### GET `/api/stats`

```typescript
// Response
{
  "success": true,
  "stats": {
    "overview": { totalRecords, totalCountries, averageRating },
    "byCategory": { hotel: 1200, restaurant: 1500, ... },
    "byCountry": { Indonesia: 1500, Thailand: 1200, ... }
  }
}
```

### Internal API Proxy

All external API calls from client go through proxy:

```typescript
// Client-side
const response = await fetch('/api/proxy', {
  method: 'POST',
  body: JSON.stringify({
    protocol: 'https',
    origin: 'api.example.com',
    path: '/endpoint',
    method: 'GET',
    headers: {},
  }),
});
```

---

## Real-time Collaboration

### SpacetimeDB Integration

```typescript
// Connection
import { SpacetimeDBClient } from '@clockworklabs/spacetimedb-sdk';

const client = new SpacetimeDBClient(
  'wss://your-database.spacetimedb.com',
  'stc-datahub'
);

// Subscribe to tables
client.subscribe([
  'SELECT * FROM CollabUser',
  'SELECT * FROM DataChange',
]);

// React hook
export function useCollabUsers() {
  const [users, setUsers] = useState<CollabUser[]>([]);
  
  useEffect(() => {
    const unsubscribe = client.on('CollabUser', (user) => {
      setUsers(prev => [...prev, user]);
    });
    
    return unsubscribe;
  }, []);
  
  return users;
}
```

---

## Security

### API Security

- **CORS**: Configured for safe cross-origin requests
- **Input Validation**: All API inputs validated and sanitized
- **Rate Limiting**: (Planned) Prevent abuse
- **SQL Injection**: Not applicable (no SQL, using SpacetimeDB)

### Client Security

- **XSS Prevention**: React automatically escapes content
- **CSRF Protection**: Next.js built-in protection
- **Content Security Policy**: (Recommended to add)

```typescript
// next.config.js
const securityHeaders = [
  {
    key: 'X-Content-Type-Options',
    value: 'nosniff',
  },
  {
    key: 'X-Frame-Options',
    value: 'SAMEORIGIN',
  },
];
```

---

## Performance

### Optimization Strategies

1. **Code Splitting**: Automatic with Next.js App Router
2. **Lazy Loading**: Dynamic imports for heavy components
3. **Memoization**: React.memo for expensive renders
4. **Virtualization**: For large data tables (planned)
5. **Edge Functions**: API routes run on Vercel Edge

### Caching Strategy

```typescript
// API caching
export async function GET(request: Request) {
  return new Response(JSON.stringify(data), {
    headers: {
      'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300',
    },
  });
}

// Client-side caching
const cache = new Map<string, { data: any; timestamp: number }>();
```

---

## Scalability

### Horizontal Scaling

- **Vercel Edge**: Automatically scales globally
- **SpacetimeDB**: Distributed database architecture
- **CDN**: Static assets served via CDN

### Data Handling

- **Pagination**: Limit data fetches to manageable chunks
- **Streaming**: (Planned) Stream large exports
- **Background Processing**: (Planned) Offload heavy processing

### Future Improvements

- Redis cache for API responses
- Queue system for batch processing
- Database sharding for large datasets
- GraphQL for flexible queries

---

## Testing Strategy (Planned)

```typescript
// Unit tests
describe('DataExportUtils', () => {
  it('exports to CSV format', () => {
    const data = [{ id: '1', name: 'Test' }];
    const csv = exportToCSV(data);
    expect(csv).toContain('id,name');
  });
});

// Integration tests
describe('API /data-share', () => {
  it('returns paginated data', async () => {
    const response = await fetch('/api/data-share?page=1&limit=10');
    const data = await response.json();
    expect(data.pagination.page).toBe(1);
  });
});

// E2E tests
describe('User workflow', () => {
  it('creates connector and fetches data', async () => {
    // Playwright test
  });
});
```

---

## Monitoring & Observability

### Metrics to Track

- API response times
- Error rates
- User sessions
- Real-time connections
- Data processing throughput

### Logging

```typescript
export function logEvent(event: string, metadata: any): void {
  console.log(JSON.stringify({
    timestamp: new Date().toISOString(),
    event,
    metadata,
  }));
}
```

---

## Future Architecture Considerations

1. **Microservices**: Break processing pipeline into separate services
2. **Message Queue**: Add RabbitMQ/Kafka for async processing
3. **GraphQL**: Alternative to REST API
4. **Mobile App**: React Native version
5. **Desktop App**: Electron wrapper
6. **AI/ML Pipeline**: Dedicated service for AI insights

---

**Architecture Documentation v1.0.0**  
Last Updated: October 2025
