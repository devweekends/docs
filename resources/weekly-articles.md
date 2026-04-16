# Weekly Engineering Articles/Talks - Learning Resources

---

## JavaScript & Frontend
*Understanding the runtime, UI layer, and design principles for client-side development.*

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

## Backend & Databases
*Server-side architecture, data modeling, and database engineering.*

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

### PostgreSQL Index Types: GIN vs GiST vs pg_trgm
**Link:** https://chatgpt.com/share/69de5812-c2a8-83ab-8587-1fd69fee8df7

A practical deep-dive into PostgreSQL's advanced index types. **GIN** (Generalized Inverted Index) is ideal for full-text search and JSONB queries it indexes every element inside a composite value. **GiST** (Generalized Search Tree) is better suited for geometric data, range types, and nearest-neighbor searches. **pg_trgm** is a trigram-based extension that enables fuzzy `LIKE`/`ILIKE` search and similarity matching on text columns. Understanding when to use each is critical for optimizing search performance in Postgres.

### MySQL Multi-Master Replication
**Link:** https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-replication-multi-master.html

Official MySQL docs on multi-master (multi-primary) replication conflict handling, binlog, and circular replication topologies. Foundational for understanding database HA patterns.

### ACID Properties
**Link:** https://en.wikipedia.org/wiki/ACID

Defines Atomicity, Consistency, Isolation, and Durability the four properties that guarantee reliable database transactions. Good starting point; follow up with Hussein Nasser's DB fundamentals for depth.

### Bloom Filter
**Link:** https://en.wikipedia.org/wiki/Bloom_filter

A probabilistic data structure that tests set membership with no false negatives but possible false positives. Used in databases (Cassandra, BigTable) to avoid unnecessary disk reads.

### Multi-Master Replication
**Link:** https://en.wikipedia.org/wiki/Multi-master_replication

Overview of multi-master replication patterns and conflict resolution strategies. Relevant to geo-distributed databases.

### NoSQL Should You Go Beyond Relational? Treehouse
**Link:** https://blog.teamtreehouse.com/should-you-go-beyond-relational-databases

A beginner-friendly intro to when to choose NoSQL over SQL. Good for framing the decision, but lacks depth follow up with the Baqend NoSQL Survey (in weekly-articles.md Database section).

### Caching Strategies Codeahoy
**Link:** https://codeahoy.com/2017/08/11/caching-strategies-and-how-to-choose-the-right-one/

A practical walkthrough of caching patterns: Cache-Aside, Write-Through, Write-Behind, and Read-Through. Useful as a mid-level intro to caching strategy trade-offs.

### SSTable and Log-Structured Storage: LevelDB Ilya Grigorik
**Link:** https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/

Written by a Google Chrome performance engineer. Deep-dives into how SSTables and LSM-Trees work in LevelDB the same concepts behind Cassandra, RocksDB, and HBase's storage engines. Essential for understanding how modern databases store data on disk.

### Original Cassandra Paper Cornell / Facebook
**Link:** http://www.cs.cornell.edu/Projects/ladis2009/papers/Lakshman-ladis2009.PDF

The original academic paper introducing Apache Cassandra. Written by Facebook engineers and published at Cornell's LADIS workshop. Explains the design decisions for a highly available, decentralized, structured storage system at massive scale.

---

## System Design & Architecture
*Scaling, distributed systems, and real-world architecture case studies.*

### Monoliths and Microservices
**Link:** https://medium.com/@SkyscannerEng/monoliths-and-microservices-8c65708c3dbf

The choice between monolithic and microservices architecture depends on organizational complexity. Monoliths are easier to develop and debug; Microservices offer scale and autonomy but introduce distributed system complexity.

### Load Balancing Fundamentals
**Link:** https://youtu.be/K0Ta65OqQkY

Load balancing distributes traffic to prevent server overload. This covers Layer 4 (Transport) vs Layer 7 (Application) balancing and algorithms like Round Robin and Least Connections.

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

### High-Level Design (HLD) Case Studies
*Applying system design principles to real-world problems.*

#### Social & Media
* **Design a URL Shortener (TinyURL):** [Base62 encoding, high read throughput.](https://resources.devweekends.com/system-design/case-url-shortener)
* **Design Twitter/X Timeline:** [Fan-out on Write vs Read, Hybrid feeds.](https://resources.devweekends.com/system-design/case-twitter)
* **Design Instagram/Flickr:** [Blob storage, CDN, Metadata separation.](https://medium.com/@lazygeek78/system-design-series-cfa60db16c27)
* **Design WhatsApp:** [Real-time delivery, Offline inbox, Websockets.](https://resources.devweekends.com/system-design/case-whatsapp#design-whatsapp-messenger)
* **Design YouTube:** [Video chunking, Adaptive streaming, CDNs.](https://resources.devweekends.com/system-design/case-netflix)

#### Services & Utilities
* **Design Uber/Lyft:** [QuadTrees, Geospatial indexing, Matching.](https://resources.devweekends.com/system-design/case-uber#design-uber-lyft)
* **Design Google Drive:** [Block-level deduplication, Synchronization.](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox)
* **Design a Rate Limiter:** [Token Bucket, Leaky Bucket, Distributed counters.](https://resources.devweekends.com/system-design/case-rate-limiter)
* **Design Notification System:** [Priority queues, Pluggable providers.](https://resources.devweekends.com/system-design/case-notification-system)
* **Design Search Autocomplete:** [Tries, Top-K queries, Typeahead.](https://www.geeksforgeeks.org/system-design/googles-search-autocomplete-high-level-designhld/)

### Amazon Dynamo Paper (SOSP 2007)
**Link:** https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf

The foundational distributed key-value store paper by Amazon's engineers. Introduces eventual consistency, consistent hashing, vector clocks, and the architecture that inspired DynamoDB, Cassandra, and Riak. An absolute must-read for anyone serious about distributed systems.

### Differential Synchronization Neil Fraser (Google)
**Link:** https://neil.fraser.name/writing/sync/

Neil Fraser's technical paper on the algorithm that powers real-time collaborative editing (like Google Docs). Explains Differential Sync, shadow copies, and how to handle concurrent edits without conflict. Exceptional and rarely discussed in typical system design resources.

### System Design Primer Donne Martin
**Link:** https://github.com/donnemartin/system-design-primer

The most comprehensive open-source resource for system design interview preparation. Covers scalability, databases, caching, messaging, load balancing, and includes worked examples of common interview problems. Start here for any system design study.

### Consistent Hashing Tom White
**Link:** https://tom-e-white.com/2007/11/consistent-hashing.html

A classic 2007 article clearly explaining how consistent hashing works and why it was a breakthrough for distributed caching. Explains the virtual nodes concept. Often cited in textbooks and papers as the go-to reference.

### What It Takes to Run Stack Overflow Nick Craver
**Link:** http://nickcraver.com/blog/2013/11/22/what-it-takes-to-run-stack-overflow

A legendary post from Stack Overflow's principal engineer. Covers their actual hardware, SQL Server setup, caching strategy, and how they serve hundreds of millions of requests with surprisingly few servers. A masterclass in pragmatic over-engineering avoidance.

### Interactive Latency Numbers Colin Scott
**Link:** https://colin-scott.github.io/personal_website/research/interactive_latency.html

Every engineer must internalize these numbers: L1 cache, RAM, SSD, network, disk. This interactive visualization (extending Jeff Dean's famous numbers) lets you explore how latency has changed across years. Reference this before every system design discussion.

### Consistent Hashing (Wikipedia)
**Link:** https://en.wikipedia.org/wiki/Consistent_hashing

Wikipedia's overview of consistent hashing. Use Tom White's article (linked in Excellent section) for better depth.

### Merkle Tree
**Link:** https://en.wikipedia.org/wiki/Merkle_tree

A hash tree where every leaf node is a hash of data. Used in Git, BitTorrent, blockchain, and distributed databases for efficient data verification and anti-entropy repair.

### Single Point of Failure (SPOF)
**Link:** https://en.wikipedia.org/wiki/Single_point_of_failure

Definition of SPOF and the importance of redundancy in system design. Good conceptual reference.

### Long Tail Distribution
**Link:** https://en.wikipedia.org/wiki/Long_tail

Useful for understanding content popularity in systems like YouTube or Netflix most content is accessed rarely, but the sum matters.

### IBM Microservices Overview
**Link:** https://www.ibm.com/cloud/learn/microservices

IBM's introductory overview of microservices architecture. Decent framing for the concept, but leans toward IBM's marketing angle. Supplement with the Skyscanner monolith/microservices article in the main list.

### Streaming Protocols DaCast
**Link:** https://www.dacast.com/blog/streaming-protocols/

Overview of video streaming protocols (HLS, DASH, RTMP). Useful for the "Design YouTube" case study, though the source is a video hosting vendor and leans marketing.

### Binary Large Object (BLOB)
**Link:** https://en.wikipedia.org/wiki/Binary_large_object

Definition and context for BLOB storage. Relevant to any media storage system design.

### Berkeley Research Paper PHT
**Link:** https://people.eecs.berkeley.edu/~sylvia/papers/pht.pdf

UC Berkeley research on Prefix Hash Trees (PHT) a distributed data structure enabling range queries over DHTs. Academic and advanced but relevant for building scalable search systems.

### Princeton SOSP 2017 Paper
**Link:** https://www.cs.princeton.edu/~wlloyd/papers/sve-sosp17.pdf

A peer-reviewed systems research paper from Princeton's SOSP 2017 proceedings. Academic-grade content on distributed systems challenges at scale.

### ArXiv Research Paper
**Link:** https://arxiv.org/pdf/0707.3670.pdf

Peer-reviewed academic research hosted on ArXiv relevant to distributed systems or data structures. Use as a deep reference for the algorithmic foundations of concepts covered in the book.

### Stanford Web Crawling Survey
**Link:** http://infolab.stanford.edu/~olston/publications/crawling_survey.pdf

A comprehensive academic survey of web crawling techniques. Covers politeness policies, URL frontier management, and distributed crawling architectures. Relevant for any system design involving large-scale data ingestion.

### Stanford CS Theory Lecture Notes
**Link:** http://theory.stanford.edu/~tim/s16/l/l1.pdf

Stanford CS theory lecture slides useful for understanding the algorithmic foundations behind consistent hashing, distributed hash tables, and data structures used in large-scale systems.

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

### Edge Functions (Cloudflare)
**Link:** https://resources.devweekends.com/aws/cdn-edge#q4-cloudfront-functions-vs-lambda-edge-when-to-use-each

Edge computing moves logic closer to the user to reduce latency. This resource covers the difference between Cloudfront Functions and Lambda@Edge, and when to use compute at the edge versus the origin server.

### GraphQL Federation
**Link:** https://resources.devweekends.com/courses/microservices-mastery/26-graphql-federation#26-graphql-federation

In microservices architectures, querying data from multiple services can be messy. GraphQL Federation allows you to build a single "Unified Graph" that acts as a gateway, aggregating data from underlying microservices transparently.

### AWS S3
**Link:** https://aws.amazon.com/s3

Official AWS S3 page. S3 is the reference implementation for durable, scalable object storage. Read this alongside any system design involving blob/media storage.

### AWS DynamoDB
**Link:** https://aws.amazon.com/dynamodb/

Official DynamoDB page. Covers single-table design, partition keys, on-demand capacity, global tables, and DynamoDB Streams. The managed implementation of the Dynamo paper.

### AWS CloudFront Dynamic Content
**Link:** https://aws.amazon.com/cloudfront/dynamic-content/

Official CloudFront docs on serving dynamic content through the CDN edge. Useful for understanding how CDNs handle more than just static assets.

### AWS EC2 High-Memory Instances
**Link:** https://aws.amazon.com/ec2/instance-types/high-memory/

Reference for understanding what hardware is available at cloud scale. Useful for back-of-the-envelope estimates during system design interviews.

### AWS Glacier FAQs
**Link:** https://aws.amazon.com/glacier/faqs/

Official FAQ for AWS Glacier (now S3 Glacier) cold archival storage. Covers retrieval times, pricing, and use cases for long-term data retention at massive scale.

### Google Cloud SLA
**Link:** https://cloud.google.com/compute/sla

Google's officially committed uptime SLAs for Compute Engine. Useful for making availability calculations during system design (e.g., five nines = 5.26 min/year downtime).

### Google Drive API Resumable Uploads
**Link:** https://developers.google.com/drive/api/v2/manage-uploads

Official Google Drive API docs on chunked, resumable file uploads. Directly relevant to the "Design Google Drive" system design case study.

### librsync Delta Compression Library
**Link:** https://github.com/librsync/librsync

The open-source library implementing the rsync rolling checksum algorithm. Relevant to file sync systems like Dropbox understanding delta sync at the binary level.

### Dropbox Security Whitepaper
**Link:** https://www.dropbox.com/static/business/resources/Security_Whitepaper.pdf

Dropbox's official security architecture whitepaper. Covers encryption at rest and in transit, key management, and data isolation relevant to the "Design Dropbox/Google Drive" interview problem.

### OSI Model
**Link:** https://en.wikipedia.org/wiki/OSI_model#Layer_architecture

The 7-layer networking model. Useful context for understanding load balancers (L4 vs L7), firewalls, and protocol design.

### Network Time Protocol (NTP)
**Link:** https://en.wikipedia.org/wiki/Network_Time_Protocol

How distributed systems synchronize clocks. Relevant to any discussion of distributed timestamps, Lamport clocks, or event ordering.

---

## APIs & Security
*Connecting services securely and enforcing access control.*

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

### Stripe Blog Rate Limiters
**Link:** https://stripe.com/blog/rate-limiters

Stripe's engineering post on how they implemented rate limiting in production. Covers Token Bucket and Fixed Window algorithms, Redis-backed distributed counters, and failure mode handling. One of the best practical write-ups on rate limiting.

### Lyft Open-Source Rate Limiter
**Link:** https://github.com/lyft/ratelimit

Lyft's open-source, production-grade rate limiting service used in Envoy Proxy. Shows how a real company implements rate limiting across a microservices mesh.

### ClassDojo Rolling Rate Limiter
**Link:** https://engineering.classdojo.com/blog/2015/02/06/rolling-rate-limiter/

A practical engineering post on implementing a sliding window rate limiter in Redis. Great complement to the Stripe rate limiter post for seeing different approaches.

### Rate Limiter GitHub Gist @ptarjan
**Link:** https://gist.github.com/ptarjan/e38f45f2dfe601419ca3af937fff574d#request-rate-limiter

A reference implementation of a request rate limiter. Concise and practical.

### REST API Tutorial Reference
**Link:** https://www.restapitutorial.com/index.html

A concise reference for HTTP status codes, methods, and REST conventions. Useful as a quick lookup when designing API contracts in system design discussions.

### Google API Rate Limits
**Link:** https://developers.google.com/docs/api/limits

Official Google API rate limiting documentation. Shows real-world quota management strategies and error handling for rate-limited APIs.

### HTTP Protocol
**Link:** https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

High-level HTTP overview. For depth, use MDN Web Docs or RFC 7230.

### UUID (Universally Unique Identifier)
**Link:** https://en.wikipedia.org/wiki/Universally_unique_identifier

Covers the different UUID versions and their collision probability. Relevant for distributed ID generation discussions.

### Unicode FAQ
**Link:** https://www.unicode.org/faq/basic_q.html

Official Unicode FAQ covering character sets, encoding (UTF-8, UTF-16), and internationalization basics. Relevant when designing systems that handle global user data.

---

## AI & Machine Learning
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

## Career & Professional Development
*Getting the job and growing as an engineer.*

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

---

## Engineering Blogs & References
*Must-follow blogs and reference materials from top engineering teams.*

### Engineering Blogs Worth Following

These are official engineering blogs from top companies bookmark and read regularly for real-world architecture patterns:

* **Uber Engineering:** http://eng.uber.com
* **High Scalability (Case Studies):** http://highscalability.com
* **Netflix Tech Blog:** https://medium.com/netflix-techblog
* **Netflix Technology Blog:** https://netflixtechblog.com/active-active-for-multi-regional-resiliency-c47719f6685b
* **Netflix Open Connect (CDN):** https://netflixtechblog.com/content-popularity-for-open-connect-b86d56f613b
* **Airbnb Engineering:** https://medium.com/airbnb-engineering
* **Stripe Engineering:** https://stripe.com/blog/engineering
* **Discord Scaling (Elixir):** https://blog.discord.com/scaling-elixir-f9b8e1e7c29b
* **Slack Engineering:** https://slack.engineering
* **LinkedIn Engineering:** https://engineering.linkedin.com/blog
* **Twitter/X Engineering:** https://blog.twitter.com/engineering/en_us.html
* **Dropbox Tech Blog:** https://blogs.dropbox.com/tech
* **Facebook/Meta Engineering:** https://code.facebook.com/posts
* **Instagram Engineering:** https://engineering.instagram.com
* **Pinterest Engineering:** https://engineering.pinterest.com
* **GitHub Engineering:** https://githubengineering.com
* **Spotify Labs:** https://labs.spotify.com
* **Shopify Engineering:** https://engineering.shopify.com
* **Yelp Engineering:** https://engineeringblog.yelp.com
* **PayPal Engineering:** https://www.paypal-engineering.com
* **Reddit Engineering:** https://redditblog.com
* **Quora Engineering:** https://engineering.quora.com
* **Asana Engineering:** https://blog.asana.com/category/eng
* **Instacart Tech:** https://tech.instacart.com
* **Nextdoor Engineering:** https://engblog.nextdoor.com
* **Atlassian Developer Blog:** https://developer.atlassian.com/blog
* **Salesforce Engineering:** https://developer.salesforce.com/blogs/engineering
* **SoundCloud Dev Blog:** https://developers.soundcloud.com/blog
* **Amazon Developer Blogs:** https://developer.amazon.com/blogs
* **Google Developers Blog:** https://developers.googleblog.com
* **Thumbtack Engineering:** https://www.thumbtack.com/engineering
* **Groupon Engineering:** https://engineering.groupon.com
* **eBay Tech Blog:** http://www.ebaytechblog.com
* **Yahoo Engineering:** https://yahooeng.tumblr.com
* **Mixpanel Blog:** https://mixpanel.com/blog
* **Cloudera Blog:** https://blog.cloudera.com
