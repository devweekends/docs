# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Overview

This repository is a [Mintlify](https://mintlify.com) documentation site for **Dev Weekends**, based on the Mintlify starter kit. It is content-focused: there is no application runtime or test suite here, only documentation content, navigation/configuration, and an example OpenAPI spec.

Production builds and hosting are handled by Mintlify via their GitHub app; pushing to the default branch triggers deployment. Local work is done using the Mintlify CLI.

## Development commands

All commands below are intended to be run from the repository root (where `docs.json` lives).

### Prerequisites

- Node.js **v19 or higher** (see `development.mdx`).
- Mintlify CLI installed globally:

```bash path=null start=null
npm i -g mint
```

### Run the local docs server

Start the Mintlify dev server on the default port (3000):

```bash path=null start=null
mint dev
```

- Serves the site at `http://localhost:3000`.
- The preview reloads automatically as MDX/JSON files change.

Run on a custom port (example: 3333):

```bash path=null start=null
mint dev --port 3333
```

If the chosen port is in use, the CLI automatically tries the next available port.

### Lint / validate docs

Validate internal links in the documentation:

```bash path=null start=null
mint broken-links
```

Use this before committing larger structural changes (renaming/moving pages, editing `docs.json`) to catch broken navigation.

### Update the Mintlify CLI

When the local preview doesn’t match production or you run into CLI issues, update the Mintlify CLI:

```bash path=null start=null
mint update
```

If you hit environment-specific CLI errors (e.g., `sharp` module issues or unknown errors), see `development.mdx` for the documented troubleshooting steps.

## High-level docs architecture

### Core configuration

- **`docs.json`** is the central site config:
  - Sets the **theme**, **site name** (`"Dev Weekends"`), brand **colors**, and favicon.
  - Defines the **sidebar navigation** via top-level `anchors`, each with `groups` and `pages`.
  - Configures **global navbar links** (e.g., `"Back to Site"` → `https://devweekends.com`).
  - Configures **footer socials** (YouTube, GitHub, LinkedIn) under `footer.socials`.
  - Defines `contextual.options` (e.g., `copy`, `view`, `chatgpt`, `claude`, `perplexity`, `mcp`, `cursor`, `vscode`) which control the contextual actions shown in the Mintlify UI.

When changing structure or branding, you almost always edit `docs.json` first, then ensure the referenced pages exist and are correctly named.

### Navigation model and content layout

Navigation is organized into **anchors** (top-level sections in the sidebar), each containing **groups**, which then reference **pages** by path. Paths map directly to `.mdx` files under this repo.

Example mapping pattern:

- A page entry like `"resources/helpful-tools"` in `docs.json` corresponds to `resources/helpful-tools.mdx`.
- Nested course structures (e.g., `courses/database-engineering/...`) are represented as groups within groups in `docs.json` and as nested folders under `courses/`.

Key anchors and their roles (high level — not an exhaustive list of pages):

- **Resources**: `resources/` — tools/utilities, learning resources, open source programs, career/company guides, weekly articles, interview prep material.
- **Interview Prep**: `resources/*-interview-qs.mdx`, `resources/interview-experiences.mdx` — question banks and experience writeups.
- **DSA Patterns**: `dsa-patterns/` — categorized algorithm patterns (arrays/strings, graphs & trees, advanced techniques like DP, backtracking, bit manipulation, etc.).
- **Courses**: `ai-engineering/`, `courses/`, `system-design/`, `engineering/`, `aws/`, `operating-systems/`, `courses/linux-internals/`, `courses/database-engineering/`, `courses/distributed-systems/`, `courses/build-your-own-x/`, `courses/c-programming/`, etc.
  - Many of these are structured as **tracks** or **modules** (e.g., “Foundations”, “Performance”, “Internals”, “Distributed”), represented as nested `group` objects in `docs.json` and matching subdirectories in `courses/`.
- **Productivity & Essentials**:
  - `productivity-sheets/overview.mdx` — productivity-related templates/resources.
  - `essentials/` — Mintlify usage docs (markdown, navigation, settings, reusable snippets, etc.) tailored to this site.
- **Top-level pages**:
  - `index.mdx` — landing page content.
  - `quickstart.mdx` — high-level onboarding for running and customizing the docs.
  - `development.mdx` — CLI usage, ports, link validation, and troubleshooting.

As a rule of thumb: if you see a path in `docs.json`, it should have a corresponding `.mdx` file; conversely, adding a new `.mdx` page only affects the site once you wire it into `docs.json` (or another page links to it directly).

### MDX content and components

All authored content is in **MDX** (`*.mdx`), mixing Markdown with JSX-like components provided by Mintlify.

Common patterns you’ll see across files:

- Layout/UX components such as `<AccordionGroup>`, `<Accordion>`, `<CardGroup>`, `<Card>`, `<Info>`, `<Steps>`, `<Step>`, `<Tip>`, `<Note>`, `<Frame>` are used to structure content, especially in onboarding docs like `quickstart.mdx` and `development.mdx`.
- Course-style content is broken into small, focused MDX files (e.g., each database-engineering module, each C programming topic, each system-design case study).
- Some pages (e.g., in `ai-tools/`) document external AI tools and workflows rather than this repo’s own behavior; they do not affect site configuration.

When editing or creating content, follow the existing patterns in nearby MDX files for component usage, heading hierarchy, and tone.

### API reference

- **OpenAPI spec**: `api-reference/openapi.json` contains an example OpenAPI 3.1 spec for a “plant store” API.
- **API docs pages**: `api-reference/` contains MDX files like:
  - `introduction.mdx` — overview of the API reference.
  - `endpoint/get.mdx`, `endpoint/create.mdx`, `endpoint/delete.mdx`, `endpoint/webhook.mdx` — endpoint-level docs that correspond to operations in `openapi.json`.

Mintlify uses the OpenAPI spec to generate structured API reference sections; the MDX files wrap and explain those endpoints, link to them, and add narrative/examples. If you extend the API:

- Update `api-reference/openapi.json` with new paths/schemas.
- Add or extend MDX files under `api-reference/` and wire them into `docs.json` as needed.

### Deployment and GitHub integration

Deployment is managed by Mintlify’s GitHub app (see README and `quickstart.mdx`):

- Install the app from the Mintlify dashboard and connect it to this repository.
- Once configured, **pushing to the default branch** triggers an automatic build and deploy of the docs site.
- There is no separate local “build” step defined in this repo; local work relies on `mint dev`, and production builds run in Mintlify’s infrastructure.

If deployment behavior appears inconsistent with local preview, first update the CLI (`mint update`), then verify `docs.json` and the relevant MDX files for structural or content issues.
