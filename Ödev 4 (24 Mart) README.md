  # Python-Selenium-Developer-Camp-2023  
  PyTest Decorator'leri aşağıdaki gibidir:
  
1-@pytest.fixture Testler için ortak bir durum oluşturur. Bu durum, her test fonksiyonu için bir kez oluşturulur ve her test fonksiyonu tarafından paylaşılır. Fixtures, ayrıca, bir testte kullanılan argümanlar gibi test verilerinin de hazırlanmasına yardımcı olabilir.

2-@pytest.mark Testlere özellikler veya etiketler eklemek için kullanılır. Örneğin, @pytest.mark.smoke etiketi, sadece hızlı ve önemli testleri içeren bir "duman testi" kategorisine atandığını belirtmek için kullanılabilir.

3-@pytest.mark.parametrize Aynı test kodunu bir dizi giriş verisiyle çalıştırmak için kullanılır. Birkaç farklı test senaryosu oluşturmak için kullanılabilir. Girdiler genellikle bir liste veya sözlük olarak verilir.

4-@pytest.mark.xfail Testin başarısız olacağını ve başarısızlığın normal olduğunu belirtmek için kullanılır. Eğer test beklenen şekilde başarısız olursa, test başarılı olarak kabul edilir ve bu başarısızlık rapor edilmez.

5-@pytest.mark.skip Belirli bir testi atlamak veya geçersiz kılmak için kullanılır. Bu, testin geçici olarak kapatıldığı durumlarda kullanışlıdır.

