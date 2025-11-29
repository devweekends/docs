# PowerShell script to create all course files
# This script creates all 28 remaining course files with their content

$ErrorActionPreference = "Stop"

# Define all course files with their content
$files = @()

# NestJS - fundamentals.mdx
$files += @{
    Path = "d:\Projects - Community\docs\courses\nestjs\fundamentals.mdx"
    Content = @"
---
title: "NestJS Fundamentals"
sidebarTitle: "1. Fundamentals"
description: "Master the core concepts and architecture of NestJS"
icon: "book"
---

# Chapter 1: NestJS Fundamentals

Learn the foundational concepts that make NestJS the most powerful Node.js framework.

## Installation & Setup

``````bash
npm install -g @nestjs/cli
nest new my-nest-app
cd my-nest-app
npm run start:dev
``````

## Core Concepts

### Controllers

``````typescript
import { Controller, Get, Post, Body, Param } from '@nestjs/common';

@Controller('users')
export class UsersController {
  @Get()
  findAll(): string {
    return 'This returns all users';
  }

  @Get(':id')
  findOne(@Param('id') id: string): string {
    return `This returns user #${id}`;
  }

  @Post()
  create(@Body() createUserDto: any): string {
    return 'This creates a new user';
  }
}
``````

### Providers (Services)

``````typescript
import { Injectable } from '@nestjs/common';

@Injectable()
export class UsersService {
  private users = [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
  ];

  findAll() {
    return this.users;
  }

  findOne(id: number) {
    return this.users.find(user => user.id === id);
  }

  create(user: any) {
    const newUser = { id: this.users.length + 1, ...user };
    this.users.push(newUser);
    return newUser;
  }
}
``````

### Modules

``````typescript
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';

@Module({
  controllers: [UsersController],
  providers: [UsersService],
  exports: [UsersService],
})
export class UsersModule {}
``````

---

<Card title="Chapter 2: Dependency Injection" icon="arrow-right" href="/courses/nestjs/dependency-injection">
  Learn about NestJS's powerful dependency injection system
</Card>
"@
}

Write-Host "Creating all course files..."
$count = 0

foreach ($file in $files) {
    try {
        $dir = Split-Path $file.Path -Parent
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
        
        Set-Content -Path $file.Path -Value $file.Content -Encoding UTF8
        $count++
        Write-Host "Created: $($file.Path)"
    }
    catch {
        Write-Host "Error creating $($file.Path): $_" -ForegroundColor Red
    }
}

Write-Host "`nTotal files created: $count" -ForegroundColor Green
