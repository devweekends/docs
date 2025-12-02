# DevOps Tools Course - Navigation Update

## Manual Action Required

Add the following JSON to `docs.json` after the C Programming course group (around line 710, after the closing brace of C Programming):

```json
,
{
  "group": "DevOps Tools",
  "icon": "toolbox",
  "pages": [
    "courses/devops-tools/overview",
    {
      "group": "Git Crash Course",
      "pages": [
        "courses/devops-tools/git-overview",
        "courses/devops-tools/git-fundamentals",
        "courses/devops-tools/git-branching",
        "courses/devops-tools/git-collaboration",
        "courses/devops-tools/git-advanced",
        "courses/devops-tools/git-workflows",
        "courses/devops-tools/git-hooks"
      ]
    },
    {
      "group": "Linux Crash Course",
      "pages": [
        "courses/devops-tools/linux-overview",
        "courses/devops-tools/linux-fundamentals",
        "courses/devops-tools/linux-permissions",
        "courses/devops-tools/linux-processes",
        "courses/devops-tools/linux-networking",
        "courses/devops-tools/linux-scripting",
        "courses/devops-tools/linux-monitoring",
        "courses/devops-tools/linux-security"
      ]
    },
    {
      "group": "Docker Crash Course",
      "pages": [
        "courses/devops-tools/docker-overview",
        "courses/devops-tools/docker-fundamentals",
        "courses/devops-tools/docker-images",
        "courses/devops-tools/docker-networking",
        "courses/devops-tools/docker-compose",
        "courses/devops-tools/docker-best-practices"
      ]
    },
    {
      "group": "RabbitMQ Crash Course",
      "pages": [
        "courses/devops-tools/rabbitmq-overview",
        "courses/devops-tools/rabbitmq-fundamentals",
        "courses/devops-tools/rabbitmq-patterns",
        "courses/devops-tools/rabbitmq-reliability"
      ]
    },
    {
      "group": "Kafka Crash Course",
      "pages": [
        "courses/devops-tools/kafka-overview",
        "courses/devops-tools/kafka-fundamentals",
        "courses/devops-tools/kafka-producers-consumers",
        "courses/devops-tools/kafka-streams",
        "courses/devops-tools/kafka-operations"
      ]
    },
    {
      "group": "Kubernetes Crash Course",
      "pages": [
        "courses/devops-tools/kubernetes-overview",
        "courses/devops-tools/kubernetes-fundamentals",
        "courses/devops-tools/kubernetes-workloads",
        "courses/devops-tools/kubernetes-services",
        "courses/devops-tools/kubernetes-config",
        "courses/devops-tools/kubernetes-storage",
        "courses/devops-tools/kubernetes-windows-linux"
      ]
    }
  ]
}
```

## Where to Add

1. Open `d:\Projects - Community\docs\docs.json`
2. Find the C Programming course group (ends around line 710)
3. After the closing brace `}` of C Programming, add a comma `,`
4. Paste the JSON above
5. Save the file

## Files Created So Far

### ✅ Complete - Git Crash Course
- overview.mdx
- git-overview.mdx (History, importance, learning path)
- git-fundamentals.mdx (Installation, basic workflow, commits)
- git-branching.mdx (Branching strategies, merging, conflicts)
- git-collaboration.mdx (Remotes, pull requests, code review)
- git-advanced.mdx (Rebase, cherry-pick, stash, reflog, internals)

### ✅ SVG Diagrams (Light Theme)
- git-workflow.svg
- git-branching.svg
- git-distributed.svg

### ⏳ Pending - Other Crash Courses
The remaining 5 crash courses (Linux, Docker, RabbitMQ, Kafka, Kubernetes) with their respective modules and SVG diagrams still need to be created following the same pattern.

## Next Steps

1. Manually add the navigation JSON to docs.json
2. Continue creating remaining crash course modules
3. Generate additional SVG diagrams for each tool
4. Test all links and navigation

The Git crash course is complete and serves as the template for the remaining courses!
