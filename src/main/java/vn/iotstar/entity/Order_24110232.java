package vn.iotstar.entity;

import java.io.Serializable;
import java.util.Date;
import java.util.List;
import javax.persistence.*;

@Entity
@Table(name = "Orders")
public class Order_24110232 implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int orderId;
    
    private String customerName;
    private String address;
    private String phone;
    private String paymentMethod; // e.g. "COD"
    
    @Temporal(TemporalType.TIMESTAMP)
    private Date orderDate;
    
    private int status; // 0: pending

    @OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
    private List<OrderDetail_24110232> orderDetails;

    public int getOrderId() { return orderId; }
    public void setOrderId(int orderId) { this.orderId = orderId; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getPaymentMethod() { return paymentMethod; }
    public void setPaymentMethod(String paymentMethod) { this.paymentMethod = paymentMethod; }
    public Date getOrderDate() { return orderDate; }
    public void setOrderDate(Date orderDate) { this.orderDate = orderDate; }
    public int getStatus() { return status; }
    public void setStatus(int status) { this.status = status; }
    public List<OrderDetail_24110232> getOrderDetails() { return orderDetails; }
    public void setOrderDetails(List<OrderDetail_24110232> orderDetails) { this.orderDetails = orderDetails; }
}
