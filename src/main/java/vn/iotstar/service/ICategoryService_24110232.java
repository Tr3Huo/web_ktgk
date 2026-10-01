package vn.iotstar.service;

import java.util.List;
import vn.iotstar.entity.Category_24110232;

public interface ICategoryService_24110232 {
    List<Category_24110232> findAll();
    Category_24110232 findById(int categoryId);
}
