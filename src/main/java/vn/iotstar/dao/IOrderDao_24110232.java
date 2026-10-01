package vn.iotstar.dao;

import java.util.List;
import vn.iotstar.entity.Order_24110232;

public interface IOrderDao_24110232 {
    List<Order_24110232> findAll();
    List<Order_24110232> findByPhone(String phone);
    List<Order_24110232> findByPhoneAndStatus(String phone, int status);
    List<Order_24110232> findByUser(String username);
    List<Order_24110232> findByUserAndStatus(String username, int status);
    Order_24110232 findById(int id);
    void updateStatus(int orderId, int status);
}
