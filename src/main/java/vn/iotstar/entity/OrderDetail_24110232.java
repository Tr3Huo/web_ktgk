package vn.iotstar.entity;

import java.io.Serializable;
import javax.persistence.*;

@Entity
@Table(name = "OrderDetails")
public class OrderDetail_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int detailId;

    @ManyToOne
    @JoinColumn(name = "orderId")
    private Order_24110232 order;

    @ManyToOne
    @JoinColumn(name = "videoId")
    private Video_24110232 video;

    private int quantity;

    public int getDetailId() { return detailId; }
    public void setDetailId(int detailId) { this.detailId = detailId; }
    public Order_24110232 getOrder() { return order; }
    public void setOrder(Order_24110232 order) { this.order = order; }
    public Video_24110232 getVideo() { return video; }
    public void setVideo(Video_24110232 video) { this.video = video; }
    public int getQuantity() { return quantity; }
    public void setQuantity(int quantity) { this.quantity = quantity; }
}
