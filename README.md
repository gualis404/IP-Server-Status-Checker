# IP-Server-Status-Checker

Python ile belirli bir IP adresi aralığına sahip rastgele IP adreslerini oluşturarak her bir IP adresine HTTP isteği gönderir. Herhangi bir IP adresine bir HTTP isteği göndermek, o sunucudan yanıt almayı amaçlar. Eğer yanıt alınabilirse, sunucunun yanıt verdiği durum koduna ve sunucunun hangi yazılımı kullandığına bakarak sunucunun durumu hakkında bilgi toplar.
<br>
<br>
Ayrıca, her IP adresi için "ipinfo.io" API'sini kullanarak IP adresinin ülkesini belirlemeye çalışır. Bu sayede, IP adresinin hangi ülkede olduğu hakkında daha fazla bilgi edinilebilir.
<br>
<br>
Kod, çoklu iş parçacıklar (CPU) kullanarak hızlı bir şekilde birçok IP adresine istek gönderir ve yanıtları toplar. Kodun çalıştırılması için kullanıcıdan istek sayısı girilmesi gerekmektedir.

