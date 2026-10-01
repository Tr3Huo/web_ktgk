package vn.iotstar.entity;

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

    @Column(name = "Fullname", columnDefinition = "NVARCHAR(50)")
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
