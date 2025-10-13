# 🤝 Contributing to STC DataHub

Thank you for your interest in contributing to STC DataHub! We welcome contributions from the community.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

---

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm
- Git
- Code editor (VS Code recommended)
- Basic knowledge of TypeScript, React, and Next.js
- SpacetimeDB CLI (optional, for collaboration features)

### Find an Issue

1. Check [GitHub Issues](https://github.com/mrbrightsides/rantai-datahub/issues)
2. Look for issues tagged with `good-first-issue` or `help-wanted`
3. Comment on the issue to claim it
4. Wait for maintainer approval before starting work

---

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/stc-datahub.git
cd stc-datahub
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### 4. SpacetimeDB Setup (Optional)

```bash
# Install SpacetimeDB
curl --proto '=https' --tlsv1.2 -sSf https://install.spacetimedb.com | sh

# Start local server
spacetime start

# Publish module
cd spacetime-server
spacetime publish stc-datahub --clear-database
```

---

## How to Contribute

### Types of Contributions

1. **🐛 Bug Fixes** - Fix issues and improve stability
2. **✨ Features** - Add new functionality
3. **📝 Documentation** - Improve docs and examples
4. **🎨 UI/UX** - Enhance user interface
5. **🧪 Tests** - Add or improve test coverage
6. **♻️ Refactoring** - Code improvements without changing behavior
7. **🌐 Translations** - Add or improve i18n translations

### Contribution Workflow

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make changes**
   - Write clean, documented code
   - Follow coding standards
   - Add tests if applicable

3. **Commit changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Fill in the PR template
   - Wait for review

---

## Coding Standards

### TypeScript

- **Strict typing**: Always use explicit types
- **No `any`**: Avoid implicit or explicit `any` types
- **Interfaces first**: Define interfaces for complex types
- **Type imports**: Use `import type` for type-only imports

```typescript
// ✅ Good
interface TourismData {
  id: string;
  name: string;
  rating: number;
}

function processData(data: TourismData): void {
  // implementation
}

// ❌ Bad
function processData(data: any) {
  // implementation
}
```

### React Components

- **Functional components**: Use function components with hooks
- **Props typing**: Always type component props
- **Component naming**: PascalCase for components
- **File naming**: kebab-case for files

```typescript
// ✅ Good
interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

export function Button({ label, onClick, disabled = false }: ButtonProps): JSX.Element {
  return (
    <button onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}

// ❌ Bad
export function Button(props: any) {
  return <button onClick={props.onClick}>{props.label}</button>;
}
```

### File Organization

```
src/
├── app/                  # Next.js pages
├── components/           # React components
│   ├── ui/              # Reusable UI components
│   ├── dashboard/       # Dashboard-specific
│   └── visualization/   # Charts, maps, etc.
├── lib/                 # Utilities and helpers
├── hooks/               # Custom React hooks
└── types/               # TypeScript type definitions
```

### Naming Conventions

- **Variables**: camelCase
- **Functions**: camelCase
- **Components**: PascalCase
- **Constants**: UPPER_SNAKE_CASE
- **Files**: kebab-case
- **Types/Interfaces**: PascalCase

---

## Commit Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
# Feature
git commit -m "feat(maps): add heatmap visualization"

# Bug fix
git commit -m "fix(export): resolve CSV encoding issue"

# Documentation
git commit -m "docs(api): update API endpoint documentation"

# Refactoring
git commit -m "refactor(dashboard): extract widget components"
```

---

## Pull Request Process

### Before Submitting

1. ✅ Update documentation if needed
2. ✅ Add tests for new features
3. ✅ Ensure all tests pass: `npm run build`
4. ✅ Follow code style guidelines
5. ✅ Update CHANGELOG.md (for significant changes)

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How to test the changes

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No new warnings
```

### Review Process

1. **Automated checks**: CI/CD pipeline must pass
2. **Code review**: At least one maintainer approval required
3. **Changes requested**: Address feedback and push updates
4. **Approval**: Maintainer will merge the PR

---

## Testing

### Running Tests

```bash
# Build test (type checking)
npm run build

# Lint
npm run lint
```

### Writing Tests

- Test files should be colocated with source files
- Use descriptive test names
- Cover edge cases
- Mock external dependencies

```typescript
// Example test structure (when we add testing framework)
describe('DataExportUtils', () => {
  it('should export data to CSV format', () => {
    const data = [{ id: '1', name: 'Test' }];
    const csv = exportToCSV(data);
    expect(csv).toContain('id,name');
    expect(csv).toContain('1,Test');
  });
});
```

---

## Documentation

### Code Documentation

- **Functions**: Document complex logic with JSDoc comments
- **Components**: Document props and usage
- **Types**: Add descriptions for non-obvious types

```typescript
/**
 * Exports tourism data to CSV format with proper escaping
 * 
 * @param data - Array of tourism data objects
 * @param columns - Optional column selection
 * @returns CSV string with headers
 * 
 * @example
 * const csv = exportToCSV(tourismData, ['name', 'rating']);
 */
export function exportToCSV(
  data: TourismData[],
  columns?: string[]
): string {
  // implementation
}
```

### README Updates

- Update README.md for new features
- Add examples for new functionality
- Update feature list

### API Documentation

- Update API_DOCS.md for new endpoints
- Include request/response examples
- Document all parameters

---

## Feature Requests

### Submitting Feature Requests

1. Check existing issues first
2. Use feature request template
3. Provide clear use case
4. Include examples or mockups

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should this work?

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Screenshots, mockups, examples
```

---

## Bug Reports

### Submitting Bug Reports

1. Check if bug already reported
2. Use bug report template
3. Include reproduction steps
4. Provide error messages/screenshots

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Go to...
2. Click on...
3. See error

## Expected Behavior
What should happen?

## Actual Behavior
What actually happens?

## Environment
- OS: [e.g., macOS, Windows]
- Browser: [e.g., Chrome 120]
- Node version: [e.g., 18.17.0]

## Screenshots
If applicable

## Additional Context
Any other relevant information
```

---

## Questions?

- **General questions**: [GitHub Discussions](https://github.com/mrbrightsides/rantai-datahub/discussions)
- **Bug reports**: [GitHub Issues](https://github.com/mrbrightsides/rantai-datahub/issues)
- **Email**: support@elpeef.com

---

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes (for significant contributions)
- Given credit in the About section

---

**Thank you for contributing to RANTAI DataHub! 🎉**

Every contribution, no matter how small, makes a difference!
