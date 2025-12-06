# Weekly Engineering Articles/Talks - Learning Resources

## JavaScript Fundamentals & Performance
*Focus here first. Understanding the runtime (Event Loop, Memory) makes you a better React and Node developer.*

### JavaScript Execution Context
**Link:** https://dev.to/im-shafiqurehman/javascript-execution-context-made-simple-5gk0

JavaScript execution context is the environment where code is evaluated and executed. Each context has two phases: the creation phase (memory allocation, hoisting) and the execution phase. Understanding this mechanism clarifies hoisting, scope, closures, and the 'this' keyword behavior, which is fundamental to debugging complex applications.

### The Event Loop Deep Dive
**Link:** https://www.youtube.com/watch?v=8aGhZQkoFbQ

The JavaScript event loop manages asynchronous operations by continuously checking the call stack and callback queue. This resource explains the difference between Microtasks (Promises) and Macrotasks (setTimeout) and how async code actually runs, which is crucial for preventing UI blocking in complex applications.

### JavaScript Engine Architecture (V8)
**Link:** https://sujeet.pro/post/javascript/runtime/v8/#introduction

A deep dive into the V8 JavaScript engine that powers Node.js and Chrome. This covers JIT (Just-In-Time) Compilation, Inline Caching, and Hidden Classes. Understanding these internal optimization mechanisms allows developers to write code that is "engine-friendly," avoiding de-optimizations and ensuring maximum execution speed.

### Memory Management in JavaScript
**Link:** https://medium.com/@zlatkov/how-javascript-works-memory-management-how-to-handle-4-common-memory-leaks-3f28b94cfbec

Understanding memory management is critical for writing efficient code that doesn't crash servers. This resource dives into the Garbage Collection process (Mark-and-Sweep algorithm) and identifies common causes of memory leaks, such as global variables, forgotten timers, and closures.

### Handling CPU-Bound Tasks with Web Workers
**Link:** https://www.digitalocean.com/community/tutorials/how-to-handle-cpu-bound-tasks-with-web-workers

JavaScript is single-threaded. The Web Workers API solves this by enabling multithreading in browsers, allowing you to offload heavy computations (like image processing or data parsing) to separate threads. This keeps the UI responsive and prevents the page from freezing during heavy operations.

### SOLID Design Principles
**Link:** https://resources.devweekends.com/lld/solid/introduction

SOLID represents five design principles that create maintainable code: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion. These principles reduce coupling and make code easier to refactor. While originally for OOP, many concepts apply directly to modern functional component design.

### Dependency Injection Explained
**Link:** https://www.youtube.com/watch?v=J1f5b4vcxCQ

Dependency Injection is a design pattern where objects receive their dependencies from external sources rather than creating them internally. This "Inversion of Control" makes code modular and significantly easier to test using mock dependencies.

---

## React & Frontend Development
*Now that you know how JS works, apply it to the UI layer.*

### React Rendering Behavior Guide
**Link:** https://blog.isquaredsoftware.com/2020/05/blogged-answers-a-mostly-complete-guide-to-react-rendering-behavior/

React's rendering process involves queuing renders, reconciliation, and committing changes to the DOM. The article explains when and why components re-render, covering parent-child relationships and how state changes propagate through the component tree. It details optimization techniques including React.memo and useCallback.

### React State Management in 2025
**Link:** https://www.developerway.com/posts/react-state-management-2025

Modern React applications don't need traditional state management libraries for most use cases. Remote data should be handled by data-fetching libraries like TanStack Query, which solve caching and invalidation automatically. URL query parameters can be managed with routing libraries, while local component state works perfectly with useState.

### React Suspense and Data Fetching
**Link:** https://blog.logrocket.com/react-suspense-data-fetching/

React Suspense enables components to pause rendering while waiting for asynchronous data, providing a declarative way to handle loading states. It supports the render-as-you-fetch pattern, which begins rendering immediately after a network request is triggered. This eliminates waterfall requests and provides robust error handling via Error Boundaries.

### One Roundtrip Per Navigation
**Link:** https://overreacted.io/one-roundtrip-per-navigation/

Modern web applications should aim to load each page with a single network roundtrip, avoiding the common pattern of loading JavaScript before fetching data. This approach improves perceived performance by starting data requests simultaneously with page load. React Server Components and frameworks like Next.js enable this pattern.

### React Performance with Extra Layers
**Link:** https://dev.to/im-shafiqurehman/how-react-achieves-high-performance-even-with-extra-layers-339j

React maintains high performance despite its virtual DOM abstraction layer through intelligent reconciliation. The article explains the "Diffing" algorithms and the Fiber architecture, which splits rendering work into chunks to prioritize user interactions and keep the UI responsive.

### The Tao of React - Best Practices
**Link:** https://alexkondov.com/tao-of-react/

This comprehensive guide presents proven principles for building maintainable React applications. Key recommendations include favoring functional components, organizing code by feature modules rather than technical layers, keeping components focused with single responsibilities, and preferring hooks over HOCs.

### React Higher-Order Components (HOC)
**Link:** https://blog.logrocket.com/react-higher-order-components/

Higher-Order Components are functions that take a component and return an enhanced version with additional functionality. While Hooks have largely replaced HOCs for logic reuse, HOCs remain valuable for complex component transformations, authentication wrappers, and working with legacy codebases.

### React useEffect Cleanup Function
**Link:** https://blog.logrocket.com/understanding-react-useeffect-cleanup-function/

The useEffect cleanup function prevents memory leaks by canceling subscriptions, aborting fetch requests, and clearing timers before components unmount. React calls the cleanup function before running the effect on re-renders, ensuring stale effects don't persist.

### React Synthetic Events
**Link:** https://www.geeksforgeeks.org/reactjs/what-are-synthetic-events-in-reactjs

React Synthetic Events are cross-browser wrappers around native browser events that provide a consistent API across all browsers. The article explains Event Delegation (attaching one listener to the root) and how React normalizes events to ensure consistent behavior across Chrome, Firefox, and Safari.

### Optimizing with Code Splitting & Lazy Loading
**Link:** https://medium.com/@ignatovich.dm/optimizing-react-apps-with-code-splitting-and-lazy-loading-e8c8791006e3

Code splitting breaks large JavaScript bundles into smaller chunks loaded on demand. `React.lazy()` enables dynamic imports that create separate bundles automatically at build time. Route-based code splitting ensures users only download the JavaScript needed for the specific page they are viewing.

### React Design System Guide
**Link:** https://www.designsystemscollective.com/react-design-system-comprehensive-guide-1e224d2c23ff

A comprehensive React design system provides consistency, reusability, and scalability. The guide covers setting up a component library with proper documentation, theming systems, and accessibility considerations baked into every element.

### Image Optimization Techniques
**Link:** https://resources.devweekends.com/resources/frontend-interview-qs#explain-image-optimization-techniques

Images often account for the majority of page weight. This resource covers modern formats (AVIF/WebP), responsive images (srcset) to serve the correct size based on device width, and compression techniques to improve Core Web Vitals and load speed.

---

## Backend & Infrastructure
*Moving from the client to the server side.*

### Ideal Node.js Project Structure
**Link:** https://softwareontheroad.com/ideal-nodejs-project-structure

A well-organized Node.js project separates concerns into 3 layers: Controller (HTTP handling), Service (Business Logic), and Data Access (Database queries). This structure keeps logic out of routes, makes the backend testable, and allows it to scale from small APIs to enterprise applications.

### CQRS Pattern with Job Queues
**Link:** https://softwareontheroad.com/job-queues-cqrs-nodejs-mongodb-agenda/

Command Query Responsibility Segregation (CQRS) separates read and write operations into different models. Integrating job queues enables asynchronous command processing, allowing heavy write operations to be processed in the background. This improves API response times.

### Node.js Worker Threads
**Link:** https://www.youtube.com/watch?v=Gcp7triXFjg

Node.js `worker_threads` module brings true multithreading to server-side JavaScript. Each worker thread runs on its own V8 instance. This is critical for tasks like encryption or compression in production systems without blocking the main Event Loop.

### Long Polling vs SSE vs WebSockets
**Link:** https://medium.com/@asharsaleem4/long-polling-vs-server-sent-events-vs-websockets-a-comprehensive-guide-fb27c8e610d0

A comparison of real-time transport protocols. Long Polling (legacy/universal), SSE (efficient unidirectional server-to-client), and WebSockets (full bidirectional, low latency, ideal for chat/gaming).

### MERN Stack Survey Data
**Link:** https://www.linkedin.com/posts/supabase_we-surveyed-over-2000-startup-founders-activity-7374464790049624066-ydzZ

Survey data from over 2000 startup founders reveals real-world technology stack choices. The data shows how MERN compares to other popular tech stacks in terms of adoption and scalability concerns.

---

## Database Engineering
*The backend needs to store data efficiently.*

### Fundamentals of Database Engineering
**Link:** https://www.youtube.com/@hnasr

A foundational resource covering the core principles of database engineering: ACID properties (Atomicity, Consistency, Isolation, Durability), Database Internals, and detailed explanations of Isolation Levels. Essential for understanding transaction safety.

### Keys in DBMS (Primary, Foreign, Unique)
**Link:** https://webandcrafts.com/blog/keys-in-dbms

Database keys are the foundation of data integrity. Primary keys uniquely identify rows; Foreign keys create relationships between tables by referencing the primary key of another table; Unique keys ensure column values remain distinct.

### Object-Relational Mapping (ORM)
**Link:** https://www.baeldung.com/cs/object-relational-mapping

ORM bridges the gap between OOP code and Relational Tables. This resource discusses the "Impedance Mismatch," the benefits (speed of dev), and the downsides (performance overhead) of using ORMs versus raw SQL for complex queries.

### Preventing SQL Race Conditions
**Link:** https://on-systems.tech/blog/128-preventing-read-committed-sql-concurrency-errors/

Read-modify-write cycles are a common SQL anti-pattern that creates race conditions. The solution is `SELECT FOR UPDATE`, which locks rows returned by a query to ensure only one transaction can modify them at a time, preventing lost updates.

### PostgreSQL Anti-Patterns
**Link:** https://www.enterprisedb.com/blog/postgresql-anti-patterns-read-modify-write-cycles

A deep dive into concurrency in Postgres. Focuses on avoiding Read-Modify-Write cycles by pushing logic into the SQL update statement itself or using higher isolation levels (Serializable) to handle high-concurrency environments.

### NoSQL Databases: Survey & Decisions
**Link:** https://medium.baqend.com/nosql-databases-a-survey-and-decision-guidance-ea7823a822d

NoSQL databases offer diverse data models optimized for specific use cases. The survey covers Document Stores (MongoDB), Key-Value (Redis), and Graph (Neo4j) DBs, comparing performance characteristics and CAP theorem trade-offs.

### Concurrency Control Fundamentals
**Link:** https://en.wikipedia.org/wiki/Concurrency_control

Overview of locking mechanisms. Pessimistic Locking (lock before write) vs Optimistic Locking (verify version before commit). Critical for data integrity in high-traffic systems.

---

##  System Design & Architecture
*How to scale the components you've learned about so far.*

### Monoliths and Microservices
**Link:** https://medium.com/@SkyscannerEng/monoliths-and-microservices-8c65708c3dbf

The choice between monolithic and microservices architecture depends on organizational complexity. Monoliths are easier to develop and debug; Microservices offer scale and autonomy but introduce distributed system complexity.

### Load Balancing Fundamentals
**Link:** https://youtu.be/K0Ta65OqQkY

Load balancing distributes traffic to prevent server overload. This covers Layer 4 (Transport) vs Layer 7 (Application) balancing and algorithms like Round Robin and Least Connections.

### Load Balancer Use Cases
**Link:** https://www.geeksforgeeks.org/system-design/load-balancer-use-cases/

Beyond traffic distribution: utilizing Load Balancers for SSL Termination, Blue-Green Deployments, and protecting backend servers from direct internet exposure.

### Consistent Hashing Explained
**Link:** https://blog.algomaster.io/p/consistent-hashing-explained

A technique for distributed caching and sharding. Consistent hashing ensures that adding or removing a server only requires re-mapping a small fraction of keys, rather than the entire dataset. This powers systems like DynamoDB and CDNs.

### How Sharding Works
**Link:** https://medium.com/@jeeyoungk/how-sharding-works-b4dec46b3f6

Database sharding distributes data across multiple machines by partitioning based on a shard key. The article explains strategies including Range-based vs Hash-based sharding and the complexity of re-balancing data as it grows.

### CAP Theorem & PACELC
**Link:** https://resources.devweekends.com/courses/database-engineering/distributed-systems

The CAP theorem states that a distributed store can only provide two of three guarantees: Consistency, Availability, and Partition Tolerance. PACELC extends this to account for latency vs consistency trade-offs even when the system is running normally.

### Distributed Consensus (Raft/Paxos)
**Link:** https://resources.devweekends.com/courses/distributed-systems/consensus#consensus-protocols

How distributed nodes agree on truth. This resource focuses on Leader Election and Log Replication, which are the backbones of modern distributed databases.

### Transactions (2PC & Sagas)
**Link:** https://resources.devweekends.com/courses/distributed-systems/transactions#distributed-transactions

Managing transactions across microservices is complex. This resource compares Two-Phase Commit (2PC), which is a blocking protocol, against the Saga pattern, which uses a sequence of local transactions.

### Idempotency & Retries
**Link:** https://internetcomputer.org/docs/building-apps/best-practices/idempotency

In distributed networks, requests can fail. Idempotency ensures that performing the same operation multiple times (e.g., retrying a payment) produces the same result. This is crucial for safe API design.

### Scaling Uber - Case Study
**Link:** https://highscalability.com/brief-history-of-scaling-uber/

Uber's evolution from a monolithic backend to thousands of microservices. Focuses on their dispatch system, geospatial database scaling, and handling real-time data.

### Scalability Best Practices
**Link:** https://github.com/binhnguyennus/awesome-scalability

A comprehensive collection of resources covering distributed systems. Topics include database replication strategies, caching layers, message queues, circuit breakers, and backpressure mechanisms.

### Avoid Over-Engineering
**Link:** https://github.com/binhnguyennus/awesome-scalability

Over-engineering introduces unnecessary complexity. This resource emphasizes the YAGNI (You Aren't Gonna Need It) principle: start with the simplest solution that meets current requirements.

---

##  High-Level Design (HLD) Case Studies
*Applying system design principles to real-world problems.*

### Social & Media
* **Design a URL Shortener (TinyURL):** [Base62 encoding, high read throughput.](https://resources.devweekends.com/system-design/case-url-shortener)
* **Design Twitter/X Timeline:** [Fan-out on Write vs Read, Hybrid feeds.](https://resources.devweekends.com/system-design/case-twitter)
* **Design Instagram/Flickr:** [Blob storage, CDN, Metadata separation.](https://medium.com/@lazygeek78/system-design-series-cfa60db16c27)
* **Design WhatsApp:** [Real-time delivery, Offline inbox, Websockets.](https://resources.devweekends.com/system-design/case-whatsapp#design-whatsapp-messenger)
* **Design YouTube:** [Video chunking, Adaptive streaming, CDNs.](https://resources.devweekends.com/system-design/case-netflix)

### Services & Utilities
* **Design Uber/Lyft:** [QuadTrees, Geospatial indexing, Matching.](https://resources.devweekends.com/system-design/case-uber#design-uber-lyft)
* **Design Google Drive:** [Block-level deduplication, Synchronization.](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox)
* **Design a Rate Limiter:** [Token Bucket, Leaky Bucket, Distributed counters.](https://resources.devweekends.com/system-design/case-rate-limiter)
* **Design Notification System:** [Priority queues, Pluggable providers.](https://resources.devweekends.com/system-design/case-notification-system)
* **Design Search Autocomplete:** [Tries, Top-K queries, Typeahead.](https://www.geeksforgeeks.org/system-design/googles-search-autocomplete-high-level-designhld/)

---

## DevOps & Cloud
*Deploying, maintaining, and observing the architecture.*

### Dev, QA, Staging, Production Environments
**Link:** https://northflank.com/blog/what-are-dev-qa-preview-test-staging-and-production-environments

Standardizing the release pipeline. Development is for coding, QA for testing, and Staging should mirror Production exactly to catch bugs before they affect users.

### Git Internals & Workflows
**Link:** https://octobot.medium.com/how-git-internally-works-1f0932067bee

Understanding the Git Object Model (Blobs, Trees, Commits) helps resolve complex merge conflicts. This resource also compares Merge vs Rebase workflows.

### Dockerizing Applications
**Link:** https://resources.devweekends.com/courses/devops-tools/docker-best-practices

Best practices for containerization. Focuses on writing efficient Dockerfiles, using Multi-stage builds to keep images small, and ensuring consistency across environments.

### Kubernetes Architecture
**Link:** https://resources.devweekends.com/courses/devops-tools/kubernetes-fundamentals

Orchestration at scale. Covers Pods (smallest deployable units), Services (networking abstractions), and Deployments (managing state and updates) in K8s.

### Serverless Architecture
**Link:** https://www.geeksforgeeks.org/system-design/serverless-architectures/

An introduction to Function-as-a-Service (FaaS). Topics include the benefits of event-driven design, the "Cold Start" problem, and the trade-offs of stateless compute environments like AWS Lambda.

### Edge Functions (Cloudflare)
**Link:** https://resources.devweekends.com/aws/cdn-edge#q4-cloudfront-functions-vs-lambda-edge-when-to-use-each

Edge computing moves logic closer to the user to reduce latency. This resource covers the difference between Cloudfront Functions and Lambda@Edge, and when to use compute at the edge versus the origin server.

### GraphQL Federation
**Link:** https://resources.devweekends.com/courses/microservices-mastery/26-graphql-federation#26-graphql-federation

In microservices architectures, querying data from multiple services can be messy. GraphQL Federation allows you to build a single "Unified Graph" that acts as a gateway, aggregating data from underlying microservices transparently.

### WebAssembly (Wasm)
**Link:** https://en.wikipedia.org/wiki/WebAssembly

WebAssembly is a binary instruction format that allows code written in C++, Rust, or Go to run in the browser at near-native speed. It opens up the web for high-performance applications like video editing.

---

##  APIs, Security & Protocols
*Connecting the frontend, backend, and database securely.*

### REST API Design Principles
**Link:** https://restfulapi.net

Standard constraints for building web services. Covers resource modeling (URLs as nouns), statelessness, HATEOAS, and proper use of HTTP methods and status codes.

### JWT Authentication Deep Dive
**Link:** https://newsletter.systemdesign.one/p/how-jwt-works

Stateless authentication using JSON Web Tokens. Explains the Header, Payload, and Signature structure, and the security trade-offs compared to session-based auth.

### OAuth 2.0 & OIDC
**Link:** https://oauth.net/2/

The industry-standard protocol for authorization. Focuses on the Authorization Code Flow, distinguishing between Authentication (OIDC - who you are) and Authorization (OAuth - what you can do).

### HTTPS & TLS Handshake
**Link:** https://www.cloudflare.com/learning/ssl/what-is-a-tls-handshake/

Understanding how encryption in transit works. This covers the TLS handshake process, public/private key exchange, and how certificates validate server identity to prevent Man-in-the-Middle attacks.

### OWASP Top 10 Security Risks
**Link:** https://owasp.org/www-project-top-ten/

The standard awareness document for developers. It details the most critical security risks, including Injection, Broken Authentication, and Cross-Site Scripting (XSS).

### DDoS Mitigation
**Link:** https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/

Distributed Denial of Service attacks attempt to overwhelm a system. Mitigation strategies include Rate Limiting, Web Application Firewalls (WAFs), and traffic filtering.

---

##  AI/ML for Engineers
*Adding modern intelligence to your applications.*

### OpenAI API Crash Course
**Link:** https://youtu.be/xP_ZON_P4Ks

A comprehensive tutorial on integrating OpenAI's API. Learn to work with chat completions, configure parameters like temperature and max tokens, and handle streaming responses.

### Prompt Engineering for Developers
**Link:** https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/

Teaches systematic prompt engineering techniques. Covers iterative prompt development, few-shot learning, and Chain-of-Thought prompting for complex reasoning.

### Generative AI for Beginners
**Link:** https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-4-introduction-to-generative-ai-bb70f0854128

Explains generative AI fundamentals, including how models like GPT work, training processes, and the transformer architecture.

### Introduction to Generative AI (IBM)
**Link:** https://www.ibm.com/think/topics/generative-ai

IBM's overview of generative AI technology. Discusses real-world enterprise applications, governance, and security considerations crucial for adoption.

### AI/ML Foundations
**Link:** https://www.youtube.com/watch?v=TYEqenKrbaM

Foundational video breaking down AI and ML concepts. Explains the difference between supervised versus unsupervised learning and neural networks.

---

##  Career Development
*The final step: Getting the job.*

### How to Write Project Case Studies
**Link:** https://resources.devweekends.com/case-studies/overview

Effective case studies showcase your problem-solving approach. Structure: Problem → Solution → Impact. Good case studies demonstrate trade-off evaluation.

### Resume Writing Tips (XYZ Formula)
**Link:** https://www.tealhq.com/post/xyz-resume

The XYZ formula structures bullet points as "Accomplished [X] as measured by [Y] by doing [Z]." This makes your impact quantifiable and highlights the metrics hiring managers care about.

### Software Engineer's LinkedIn Guide
**Link:** https://medium.com/@wangjoshuah/the-software-engineers-guide-to-writing-a-linkedin-profile-that-stands-out-bf91d0b80ae8

Your LinkedIn profile requires strategic optimization. Use the headline for your value proposition, write a story-driven summary, and detail experience with metrics showing impact.

### Connecting with Recruiters
**Link:** https://cultivatedculture.com/linkedin-connection-requests/

LinkedIn connection requests require personalization. Reference specific roles, explain why you're interested in their company, and demonstrate research.

### ChatGPT for Job Seekers
**Link:** https://www.jeffsu.org/chatgpt-for-job-seekers-best-and-worst-use-cases/

How to use AI to accelerate job search tasks like drafting cover letters and preparing for interviews, without sounding generic or lazy.
