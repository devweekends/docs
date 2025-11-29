$courses = @{
    "nestjs" = @(
        "overview.mdx",
        "fundamentals.mdx",
        "dependency-injection.mdx",
        "controllers-routes.mdx",
        "providers-services.mdx",
        "database-integration.mdx",
        "authentication-authorization.mdx",
        "testing.mdx",
        "microservices.mdx",
        "deployment-production.mdx",
        "advanced-patterns.mdx"
    )
    "cpp-crash-course" = @(
        "overview.mdx",
        "fundamentals.mdx",
        "pointers-memory.mdx",
        "oop.mdx",
        "stl.mdx",
        "modern-cpp.mdx"
    )
    "java-crash-course" = @(
        "overview.mdx",
        "fundamentals.mdx",
        "oop.mdx",
        "collections.mdx",
        "concurrency.mdx",
        "modern-java.mdx"
    )
    "python-crash-course" = @(
        "overview.mdx",
        "fundamentals.mdx",
        "data-structures.mdx",
        "oop.mdx",
        "modules-packages.mdx",
        "advanced.mdx"
    )
}

$basePath = "d:\Projects - Community\docs\courses"

foreach ($course in $courses.Keys) {
    $coursePath = Join-Path $basePath $course
    Write-Host "Course: $course"
    Write-Host "Files to create:"
    foreach ($file in $courses[$course]) {
        $filePath = Join-Path $coursePath $file
        Write-Host "  - $file (exists: $(Test-Path $filePath))"
    }
    Write-Host ""
}

Write-Host "Total files to create: $(($courses.Values | ForEach-Object { $_.Count } | Measure-Object -Sum).Sum)"
