from django.db import models


# Create your models here.
class KerogenModel(models.Model):
    year = models.TextField(help_text="年份")
    author = models.TextField(help_text="作者")
    kerogen_type = models.TextField(help_text="干酪根类型")
    kerogen_name = models.TextField(help_text="干酪根名称")
    Kerogen_shale_molecular_formula = models.TextField(
        null=True, blank=True, help_text="干酪根/页岩结构分子式"
    )
    literature_source = models.TextField(null=True, blank=True, help_text="文献来源")
    model_element_ratio_H_C = models.TextField(
        null=True, blank=True, help_text="模型元素比H/C"
    )
    model_element_ratio_O_C = models.TextField(
        null=True, blank=True, help_text="模型元素比O/C"
    )
    model_element_ratio_N_C = models.TextField(
        null=True, blank=True, help_text="模型元素比N/C"
    )
    model_element_ratio_S_C = models.TextField(
        null=True, blank=True, help_text="模型元素比S/C"
    )
    experimental_kerogen_density = models.TextField(
        null=True,
        blank=True,
        help_text="实验干酪根的物理性质:实验干酪根密度",
    )
    simulated_kerogen_density = models.CharField(
        null=True,
        blank=True,
        help_text="干酪根模型的物理性质:模拟干酪根密度",
    )
    molecular_model_of_2d_kerogen = models.FileField(
        upload_to="kerogen_model/",
        null=True,
        blank=True,
        help_text="二维干酪根分子模型",
    )
