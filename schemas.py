"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Portfolio-specific schemas

class Project(BaseModel):
    """
    Portfolio projects
    Collection name: "project"
    """
    title: str = Field(..., description="Project title")
    summary: str = Field(..., description="Short description of the project")
    tags: List[str] = Field(default_factory=list, description="Keywords/skills")
    tech_stack: List[str] = Field(default_factory=list, description="Technologies used")
    role: Optional[str] = Field(None, description="Your role on the project")
    outcomes: Optional[str] = Field(None, description="Impact, metrics, or results")
    image_url: Optional[str] = Field(None, description="Preview image URL")
    repo_url: Optional[str] = Field(None, description="Source code repository URL")
    demo_url: Optional[str] = Field(None, description="Live demo or report link")
    year: Optional[int] = Field(None, description="Year completed")

class Message(BaseModel):
    """
    Contact messages from the portfolio
    Collection name: "message"
    """
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    subject: Optional[str] = Field(None, description="Subject line")
    message: str = Field(..., min_length=5, max_length=5000, description="Message body")
    source_page: Optional[str] = Field(None, description="Where the message was sent from")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
