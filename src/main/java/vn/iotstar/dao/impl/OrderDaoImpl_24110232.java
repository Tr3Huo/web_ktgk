package vn.iotstar.dao.impl;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.persistence.TypedQuery;
import vn.iotstar.dao.IOrderDao_24110232;
import vn.iotstar.entity.Order_24110232;
import vn.iotstar.util.JPAConfig_24110232;

public class OrderDaoImpl_24110232 implements IOrderDao_24110232 {

    @Override
    public List<Order_24110232> findAll() {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Order_24110232> query = enma.createQuery("SELECT o FROM Order_24110232 o ORDER BY o.orderDate DESC", Order_24110232.class);
        return query.getResultList();
    }

    @Override
    public List<Order_24110232> findByPhone(String phone) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Order_24110232> query = enma.createQuery("SELECT o FROM Order_24110232 o WHERE o.phone = :phone ORDER BY o.orderDate DESC", Order_24110232.class);
        query.setParameter("phone", phone);
        return query.getResultList();
    }

    @Override
    public List<Order_24110232> findByPhoneAndStatus(String phone, int status) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Order_24110232> query = enma.createQuery("SELECT o FROM Order_24110232 o WHERE o.phone = :phone AND o.status = :status ORDER BY o.orderDate DESC", Order_24110232.class);
        query.setParameter("phone", phone);
        query.setParameter("status", status);
        return query.getResultList();
    }

    @Override
    public List<Order_24110232> findByUser(String username) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        vn.iotstar.entity.User_24110232 user = enma.find(vn.iotstar.entity.User_24110232.class, username);
        String phone = (user != null && user.getPhone() != null) ? user.getPhone() : "###NULL###";
        
        TypedQuery<Order_24110232> query = enma.createQuery("SELECT o FROM Order_24110232 o LEFT JOIN o.user u WHERE u.username = :username OR o.phone = :phone ORDER BY o.orderDate DESC", Order_24110232.class);
        query.setParameter("username", username);
        query.setParameter("phone", phone);
        return query.getResultList();
    }

    @Override
    public List<Order_24110232> findByUserAndStatus(String username, int status) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        vn.iotstar.entity.User_24110232 user = enma.find(vn.iotstar.entity.User_24110232.class, username);
        String phone = (user != null && user.getPhone() != null) ? user.getPhone() : "###NULL###";
        
        TypedQuery<Order_24110232> query = enma.createQuery("SELECT o FROM Order_24110232 o LEFT JOIN o.user u WHERE (u.username = :username OR o.phone = :phone) AND o.status = :status ORDER BY o.orderDate DESC", Order_24110232.class);
        query.setParameter("username", username);
        query.setParameter("phone", phone);
        query.setParameter("status", status);
        return query.getResultList();
    }

    @Override
    public Order_24110232 findById(int id) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        return enma.find(Order_24110232.class, id);
    }

    @Override
    public void updateStatus(int orderId, int status) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        EntityTransaction trans = enma.getTransaction();
        try {
            trans.begin();
            Order_24110232 order = enma.find(Order_24110232.class, orderId);
            if(order != null) {
                order.setStatus(status);
                enma.merge(order);
            }
            trans.commit();
        } catch (Exception e) {
            e.printStackTrace();
            trans.rollback();
            throw e;
        } finally {
            enma.close();
        }
    }
}
