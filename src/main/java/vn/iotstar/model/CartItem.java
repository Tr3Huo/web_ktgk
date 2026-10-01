package vn.iotstar.model;

import java.io.Serializable;
import vn.iotstar.entity.Video_24110232;

public class CartItem implements Serializable {
    private static final long serialVersionUID = 1L;
    
    private Video_24110232 video;
    private int quantity;

    public CartItem() {
    }

    public CartItem(Video_24110232 video, int quantity) {
        this.video = video;
        this.quantity = quantity;
    }

    public Video_24110232 getVideo() {
        return video;
    }

    public void setVideo(Video_24110232 video) {
        this.video = video;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}
