package vn.iotstar.service.impl;

import java.util.List;
import vn.iotstar.dao.ICategoryDao_24110232;
import vn.iotstar.dao.impl.CategoryDaoImpl_24110232;
import vn.iotstar.entity.Category_24110232;
import vn.iotstar.service.ICategoryService_24110232;

public class CategoryServiceImpl_24110232 implements ICategoryService_24110232 {
    ICategoryDao_24110232 categoryDao = new CategoryDaoImpl_24110232();

    @Override
    public List<Category_24110232> findAll() {
        return categoryDao.findAll();
    }

    @Override
    public Category_24110232 findById(int categoryId) {
        return categoryDao.findById(categoryId);
    }
}
