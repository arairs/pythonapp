curl -X POST http://127.0.0.1:5000/item -H "Content-Type: application/json" -d '{"item": "Iara", "Status":"Iniciado"}'
curl -X GET http://127.0.0.1:5000/item
curl -X PATCH http://127.0.0.1:5000/1 -H "Content-Type: application/json" -d '{"item": "panqueca", "Status":"Finalizado"}'
curl -X DELETE http://127.0.0.1:5000/item/1

curl -X POST https://api.zerosheets.com/v1/yfr -H "Content-Type: application/json" -d '{"item": "Iara", "Status":"Iniciado"}'
curl -X GET https://api.zerosheets.com/v1/yfr
curl -X PATCH https://api.zerosheets.com/v1/yfr/28 -H "Content-Type: application/json" -d '{"item": "panqueca", "Status":"Finalizado"}'
curl -X DELETE https://api.zerosheets.com/v1/yfr/28
