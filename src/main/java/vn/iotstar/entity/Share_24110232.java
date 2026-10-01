package vn.iotstar.entity;

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
