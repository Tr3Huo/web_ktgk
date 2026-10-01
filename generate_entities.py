import os

path = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\src\main\java\vn\iotstar\entity'
if not os.path.exists(path):
    os.makedirs(path)

entities = {
    'User_24110232.java': """package vn.iotstar.entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;

@Entity
@Table(name = "Users")
public class User_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @Column(name = "Username", length = 50)
    private String username;

    @Column(name = "Password", length = 50)
    private String password;

    @Column(name = "Phone", length = 15)
    private String phone;

    @Column(name = "Fullname", length = 50)
    private String fullname;

    @Column(name = "Email", length = 150)
    private String email;

    @Column(name = "Admin")
    private Boolean admin;

    @Column(name = "Active")
    private Boolean active;

    @Column(name = "Images", length = 500)
    private String images;

    @OneToMany(mappedBy = "user")
    private List<Share_24110232> shares;

    @OneToMany(mappedBy = "user")
    private List<Favorite_24110232> favorites;

    // Getters and Setters
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getFullname() { return fullname; }
    public void setFullname(String fullname) { this.fullname = fullname; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public Boolean getAdmin() { return admin; }
    public void setAdmin(Boolean admin) { this.admin = admin; }
    public Boolean getActive() { return active; }
    public void setActive(Boolean active) { this.active = active; }
    public String getImages() { return images; }
    public void setImages(String images) { this.images = images; }
    public List<Share_24110232> getShares() { return shares; }
    public void setShares(List<Share_24110232> shares) { this.shares = shares; }
    public List<Favorite_24110232> getFavorites() { return favorites; }
    public void setFavorites(List<Favorite_24110232> favorites) { this.favorites = favorites; }
}
""",
    'Category_24110232.java': """package vn.iotstar.entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;

@Entity
@Table(name = "Category")
public class Category_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "CategoryId")
    private int categoryId;

    @Column(name = "Categoryname", length = 100)
    private String categoryname;

    @Column(name = "Categorycode", length = 100)
    private String categorycode;

    @Column(name = "Images", length = 500)
    private String images;

    @Column(name = "Status")
    private Boolean status;

    @OneToMany(mappedBy = "category")
    private List<Video_24110232> videos;

    // Getters and Setters
    public int getCategoryId() { return categoryId; }
    public void setCategoryId(int categoryId) { this.categoryId = categoryId; }
    public String getCategoryname() { return categoryname; }
    public void setCategoryname(String categoryname) { this.categoryname = categoryname; }
    public String getCategorycode() { return categorycode; }
    public void setCategorycode(String categorycode) { this.categorycode = categorycode; }
    public String getImages() { return images; }
    public void setImages(String images) { this.images = images; }
    public Boolean getStatus() { return status; }
    public void setStatus(Boolean status) { this.status = status; }
    public List<Video_24110232> getVideos() { return videos; }
    public void setVideos(List<Video_24110232> videos) { this.videos = videos; }
}
""",
    'Video_24110232.java': """package vn.iotstar.entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;

@Entity
@Table(name = "Videos")
public class Video_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @Column(name = "VideoId", length = 50)
    private String videoId;

    @Column(name = "Title", length = 200)
    private String title;

    @Column(name = "Poster", length = 500)
    private String poster;

    @Column(name = "Views")
    private Integer views;

    @Column(name = "Description", length = 500)
    private String description;

    @Column(name = "Active")
    private Boolean active;

    @ManyToOne
    @JoinColumn(name = "CategoryId")
    private Category_24110232 category;

    @OneToMany(mappedBy = "video", cascade = CascadeType.ALL)
    private List<Share_24110232> shares;

    @OneToMany(mappedBy = "video", cascade = CascadeType.ALL)
    private List<Favorite_24110232> favorites;

    // Getters and Setters
    public String getVideoId() { return videoId; }
    public void setVideoId(String videoId) { this.videoId = videoId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getPoster() { return poster; }
    public void setPoster(String poster) { this.poster = poster; }
    public Integer getViews() { return views; }
    public void setViews(Integer views) { this.views = views; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public Boolean getActive() { return active; }
    public void setActive(Boolean active) { this.active = active; }
    public Category_24110232 getCategory() { return category; }
    public void setCategory(Category_24110232 category) { this.category = category; }
    public List<Share_24110232> getShares() { return shares; }
    public void setShares(List<Share_24110232> shares) { this.shares = shares; }
    public List<Favorite_24110232> getFavorites() { return favorites; }
    public void setFavorites(List<Favorite_24110232> favorites) { this.favorites = favorites; }
}
""",
    'Share_24110232.java': """package vn.iotstar.entity;

import java.io.Serializable;
import java.util.Date;
import javax.persistence.*;

@Entity
@Table(name = "Shares")
public class Share_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ShareId")
    private int shareId;

    @Column(name = "Emails", length = 50)
    private String emails;

    @Column(name = "SharedDate")
    @Temporal(TemporalType.DATE)
    private Date sharedDate;

    @ManyToOne
    @JoinColumn(name = "Username")
    private User_24110232 user;

    @ManyToOne
    @JoinColumn(name = "VideoId")
    private Video_24110232 video;

    // Getters and Setters
    public int getShareId() { return shareId; }
    public void setShareId(int shareId) { this.shareId = shareId; }
    public String getEmails() { return emails; }
    public void setEmails(String emails) { this.emails = emails; }
    public Date getSharedDate() { return sharedDate; }
    public void setSharedDate(Date sharedDate) { this.sharedDate = sharedDate; }
    public User_24110232 getUser() { return user; }
    public void setUser(User_24110232 user) { this.user = user; }
    public Video_24110232 getVideo() { return video; }
    public void setVideo(Video_24110232 video) { this.video = video; }
}
""",
    'Favorite_24110232.java': """package vn.iotstar.entity;

import java.io.Serializable;
import java.util.Date;
import javax.persistence.*;

@Entity
@Table(name = "Favorites")
public class Favorite_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "FavoriteId")
    private int favoriteId;

    @Column(name = "LikedDate")
    @Temporal(TemporalType.DATE)
    private Date likedDate;

    @ManyToOne
    @JoinColumn(name = "VideoId")
    private Video_24110232 video;

    @ManyToOne
    @JoinColumn(name = "Username")
    private User_24110232 user;

    // Getters and Setters
    public int getFavoriteId() { return favoriteId; }
    public void setFavoriteId(int favoriteId) { this.favoriteId = favoriteId; }
    public Date getLikedDate() { return likedDate; }
    public void setLikedDate(Date likedDate) { this.likedDate = likedDate; }
    public Video_24110232 getVideo() { return video; }
    public void setVideo(Video_24110232 video) { this.video = video; }
    public User_24110232 getUser() { return user; }
    public void setUser(User_24110232 user) { this.user = user; }
}
"""
}

for name, content in entities.items():
    with open(os.path.join(path, name), 'w', encoding='utf-8') as f:
        f.write(content)

print("Entities created.")
