CREATE TABLE Users (
    Username nvarchar(50) NOT NULL PRIMARY KEY,
    Password nvarchar(50) NULL,
    Phone nvarchar(15) NULL,
    Fullname nvarchar(50) NULL,
    Email nvarchar(150) NULL,
    Admin bit NULL,
    Active bit NULL,
    Images nvarchar(500) NULL
);

CREATE TABLE Category (
    CategoryId int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Categoryname nvarchar(100) NULL,
    Categorycode nvarchar(100) NULL,
    Images nvarchar(500) NULL,
    Status bit NULL
);

CREATE TABLE Videos (
    VideoId nvarchar(50) NOT NULL PRIMARY KEY,
    Title nvarchar(200) NULL,
    Poster nvarchar(500) NULL,
    Views int NULL,
    Description nvarchar(500) NULL,
    Active bit NULL,
    CategoryId int NULL,
    FOREIGN KEY (CategoryId) REFERENCES Category(CategoryId)
);

CREATE TABLE Shares (
    ShareId int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Emails nvarchar(50) NULL,
    SharedDate date NULL,
    Username nvarchar(50) NULL,
    VideoId nvarchar(50) NULL,
    FOREIGN KEY (Username) REFERENCES Users(Username),
    FOREIGN KEY (VideoId) REFERENCES Videos(VideoId)
);

CREATE TABLE Favorites (
    FavoriteId int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    LikedDate date NULL,
    VideoId nvarchar(50) NULL,
    Username nvarchar(50) NULL,
    FOREIGN KEY (Username) REFERENCES Users(Username),
    FOREIGN KEY (VideoId) REFERENCES Videos(VideoId)
);
