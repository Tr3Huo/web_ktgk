package vn.iotstar.entity;

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

    public int getFavoriteId() { return favoriteId; }
    public void setFavoriteId(int favoriteId) { this.favoriteId = favoriteId; }
    public Date getLikedDate() { return likedDate; }
    public void setLikedDate(Date likedDate) { this.likedDate = likedDate; }
    public Video_24110232 getVideo() { return video; }
    public void setVideo(Video_24110232 video) { this.video = video; }
    public User_24110232 getUser() { return user; }
    public void setUser(User_24110232 user) { this.user = user; }
}
