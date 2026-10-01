INSERT INTO Users (Username, Password, Phone, Fullname, Email, Admin, Active, Images) VALUES
('admin', '123', '0123456789', N'Admin', 'admin@example.com', 1, 1, ''),
('user', '123', '0987654321', N'User', 'nhuthung369@gmail.com', 0, 1, '');

INSERT INTO Category (Categoryname, Categorycode, Images, Status) VALUES
(N'Giải trí', 'GIAITRI', '', 1),
(N'Học tập', 'HOCTAP', '', 1),
(N'Thể thao', 'THETHAO', '', 1);

INSERT INTO Videos (VideoId, Title, Poster, Views, Description, Active, CategoryId) VALUES
('V01', N'Video giải trí 1', '', 100, N'Mô tả video 1', 1, 1),
('V02', N'Video học tập 1', '', 50, N'Mô tả video 2', 1, 2),
('V03', N'Video thể thao 1', '', 200, N'Mô tả video 3', 1, 3),
('V04', N'Video giải trí 2', '', 150, N'Mô tả video 4', 1, 1),
('V05', N'Video học tập 2', '', 80, N'Mô tả video 5', 1, 2),
('V06', N'Video thể thao 2', '', 220, N'Mô tả video 6', 1, 3),
('V07', N'Video giải trí 3', '', 110, N'Mô tả video 7', 1, 1),
('V08', N'Video học tập 3', '', 60, N'Mô tả video 8', 1, 2);

INSERT INTO Shares (Emails, SharedDate, Username, VideoId) VALUES
('test1@example.com', '2026-09-24', 'user', 'V01'),
('test2@example.com', '2026-09-24', 'user', 'V01');

INSERT INTO Favorites (LikedDate, VideoId, Username) VALUES
('2026-09-24', 'V01', 'user'),
('2026-09-24', 'V02', 'user');
