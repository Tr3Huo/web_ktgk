package vn.iotstar.dao.impl;

import java.util.List;
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;
import vn.iotstar.dao.ICategoryDao_24110232;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.util.JPAConfig_24110232;

public class CategoryDaoImpl_24110232 implements ICategoryDao_24110232 {
    @Override
    public List<Category_24110232> findAll() {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        TypedQuery<Category_24110232> query = enma.createQuery("SELECT c FROM Category_24110232 c", Category_24110232.class);
        return query.getResultList();
    }
    
    @Override
    public Category_24110232 findById(int categoryId) {
        EntityManager enma = JPAConfig_24110232.getEntityManager();
        return enma.find(Category_24110232.class, categoryId);
    }
}
