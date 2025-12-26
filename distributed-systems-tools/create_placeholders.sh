#!/bin/bash

# Spark modules
modules=(
"spark-introduction:Introduction & Spark Foundations:1. Introduction:Learn the foundations of Apache Spark and the RDD paper"
"spark-rdd:RDD Programming & Core API:2. RDD Programming:Master Resilient Distributed Datasets and core transformations"
"spark-sql:Spark SQL & DataFrames:3. Spark SQL:High-level DataFrame API with Catalyst optimizer"
"spark-streaming:Structured Streaming:4. Streaming:Real-time data processing with Structured Streaming"
"spark-mllib:MLlib for Machine Learning:5. MLlib:Distributed machine learning at scale"
"spark-tuning:Performance Tuning:6. Performance Tuning:Optimize Spark applications for production"
"spark-operations:Cluster Deployment:7. Operations:Deploy and manage Spark in production"
"spark-advanced:Advanced Topics:8. Advanced:Delta Lake, GraphX, and ecosystem integration"
"spark-capstone:Capstone Project:9. Capstone:Build a real-time recommendation engine"
)

for module in "${modules[@]}"; do
  IFS=':' read -r filename title sidebar desc <<< "$module"
  if [ ! -f "${filename}.mdx" ]; then
    cat > "${filename}.mdx" << ENDFILE
---
title: "${title}"
sidebarTitle: "${sidebar}"
description: "${desc}"
icon: "bolt"
---

# ${title}

<Info>
**Module Duration**: 4-5 hours
**Focus**: Core Spark concepts and hands-on examples
**Prerequisites**: Previous modules or distributed systems basics
</Info>

## Coming Soon

This module is currently under development. Check back soon for:

- Comprehensive theory and concepts
- Hands-on code examples in Scala and PySpark
- Real-world use cases and patterns
- Performance optimization techniques
- Interview preparation topics

## What You'll Learn

Detailed content covering ${title} will be added here, including:
- Core concepts and architecture
- Practical code examples
- Best practices and patterns
- Common pitfalls to avoid

---

<Note>
This is a placeholder. Full content will be available soon.
</Note>
ENDFILE
  fi
done

# Flink modules
flink_modules=(
"flink-introduction:Introduction & Streaming Foundations:1. Introduction:Learn true stream processing fundamentals"
"flink-datastream:DataStream API:2. DataStream API:Master the low-level streaming API"
"flink-eventtime:Event Time & Watermarks:3. Event Time:Handle out-of-order events with watermarks"
"flink-windows:Windows & Time Operations:4. Windows:Time-based aggregations and windowing"
"flink-state:Stateful Stream Processing:5. State:Managed state and fault tolerance"
"flink-sql:Table API & Flink SQL:6. SQL:Declarative stream processing"
"flink-cep:Complex Event Processing:7. CEP:Pattern detection in event streams"
"flink-operations:Production Deployment:8. Operations:Deploy and monitor Flink clusters"
"flink-capstone:Capstone Project:9. Capstone:Build a fraud detection system"
)

for module in "${flink_modules[@]}"; do
  IFS=':' read -r filename title sidebar desc <<< "$module"
  if [ ! -f "${filename}.mdx" ]; then
    cat > "${filename}.mdx" << ENDFILE
---
title: "${title}"
sidebarTitle: "${sidebar}"
description: "${desc}"
icon: "wave-pulse"
---

# ${title}

<Info>
**Module Duration**: 4-5 hours
**Focus**: Stream processing with Apache Flink
**Prerequisites**: Streaming concepts, Java/Scala basics
</Info>

## Coming Soon

This module is currently under development. Check back soon for:

- Comprehensive Flink concepts
- Hands-on code examples in Java and Scala
- Real-time streaming patterns
- State management techniques
- Production deployment strategies

## What You'll Learn

Detailed content covering ${title} will be added here, including:
- Core Flink architecture
- Practical implementations
- Advanced streaming patterns
- Performance optimization

---

<Note>
This is a placeholder. Full content will be available soon.
</Note>
ENDFILE
  fi
done

# Beam modules
beam_modules=(
"beam-introduction:Introduction & Dataflow Model:1. Introduction:Learn the unified batch/streaming model"
"beam-core:Core Programming Model:2. Core Model:Master PCollections and ParDo"
"beam-windowing:Windowing & Time:3. Windowing:Time-based processing strategies"
"beam-triggers:Triggers & Watermarks:4. Triggers:Control result materialization"
"beam-state:State & Timers:5. State:Stateful processing with Beam"
"beam-io:Beam I/O Connectors:6. I/O:Connect to various data sources"
"beam-sql:Beam SQL:7. SQL:Declarative data processing"
"beam-runners:Multi-Runner Execution:8. Runners:Deploy on Spark, Flink, Dataflow"
"beam-capstone:Capstone Project:9. Capstone:Build a portable ETL pipeline"
)

for module in "${beam_modules[@]}"; do
  IFS=':' read -r filename title sidebar desc <<< "$module"
  if [ ! -f "${filename}.mdx" ]; then
    cat > "${filename}.mdx" << ENDFILE
---
title: "${title}"
sidebarTitle: "${sidebar}"
description: "${desc}"
icon: "diagram-project"
---

# ${title}

<Info>
**Module Duration**: 3-4 hours
**Focus**: Portable data processing with Apache Beam
**Prerequisites**: Java or Python, basic data processing concepts
</Info>

## Coming Soon

This module is currently under development. Check back soon for:

- Beam programming model concepts
- Code examples in Java and Python SDKs
- Portable pipeline patterns
- Multi-runner deployment
- Testing strategies

## What You'll Learn

Detailed content covering ${title} will be added here, including:
- Core Beam abstractions
- Practical implementations
- Runner-independent patterns
- Production best practices

---

<Note>
This is a placeholder. Full content will be available soon.
</Note>
ENDFILE
  fi
done

echo "Placeholder files created successfully!"
