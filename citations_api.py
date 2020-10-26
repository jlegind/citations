import requests
import json
import csv


Api = 'http://cms-search.gbif.org:9200/literature/_search?q=publishingOrganizationKey:'
api = 'https://www.gbif.org/api/resource/search?contentType=literature&gbifDatasetKey='

keylist = ['4ef10600-d213-4777-835d-9e134f5f6335','2a401a87-b3e2-4de2-ab2f-e01536f69f01','6902be25-fe92-4519-a80b-a000b4b1348d','67198231-b814-491e-a1a3-870594f914f5','65d3fd1e-8dad-458b-aa30-a5c810fd4479','0eacbbfa-45b9-41dc-b7e3-1f0773ce1477','af5f680a-e0cc-46c8-b623-ceeaab70aa9e','698df663-427c-491d-8d86-8d9a2c861d9f','47f0f51f-183e-4a51-9d13-c69f2ed28c56','04d590f7-68b2-490d-b7ea-732cf66eadee','b6538814-468b-4278-b5f1-68ca4afd1e88','669671c6-83f0-4f4d-a1b4-b42799000b35','4ed38e58-77b1-4710-8c71-7d7085ecf5f4','45d532d3-ced7-4856-8590-705bc8b244a1','07bddb83-9f0c-4bc1-835e-e57bc6e17046','c65575cf-862f-448b-bef2-fc158fb2e225','769dbaf7-8238-43fa-9717-90973e41706d','5b2042ab-b98d-457b-94c3-22870cac4cfd','75f62205-c7bb-40ac-9a90-3e3d696e2c7f','2dda31ff-f776-452f-9a4b-d5229f6e3494','e1c320f6-370e-4d5e-8253-9b5285a0775f','6254b79a-5df5-4ae1-b1f0-2c8e8969b73e','2dd1b3bf-f2cd-4696-8314-8a01febc9828','1b41df21-d6a7-49fe-bdf2-2ec7b6344f88','f7fddf02-6238-4a44-bb5f-5f375e879396','882145dc-e998-4808-bb2e-c2bdd5c7edd0','dbebf070-6954-404f-af12-d61be85a99c0','2c42a5da-a059-452f-be89-dc76ec296fed','5b5deb76-1e5e-446c-9d92-6cb2ddbc9d39','fab310e8-fe27-454c-803c-ead56c22849f','d01a97f1-47a6-4627-8127-19148d698f4e','60ded084-8414-416d-856e-283345c42830','e263aa94-fc9f-4c36-bbf9-4e1864046ccd','c23c13a2-8159-4f83-be5e-cf08845b2dc1','977c2696-b7a1-4b03-a0b3-08b088f7c113','ae330c1c-212c-47ee-8078-be7274779ff1','05f10202-2407-4424-b13a-45e6376c1efb','a59ee310-03a5-43df-9737-4843b634e252','4bb5aebe-ec3b-4cf4-b0bb-ac2078dd3a19','a0c29d70-d10e-430a-81cc-730fdc4299ef','c64ea13f-f1a4-4d83-8409-d7da9b841b40','09efcc43-c674-4a70-b326-cd83f7463d1d','5788c83a-0e0a-42c1-8fcd-3b27ce7a672a','b267ac9b-6516-458e-bea7-7643842187f7','5c8ff6d3-b9dc-465a-b46a-dbb8ee30b26e','0d0f1fc9-3dff-435d-ad51-907485ea584c','ba19fc1d-670c-426b-b99d-49f003792ac4','daee2e33-786c-4162-8781-e9a75daa189f','4142ad50-b1a9-44d6-bcc2-03e8c89ec5b7','45183eb4-0416-4d4f-9439-e8146f4fdc59','6e2b3706-4e87-428d-a860-beae8ccfef9f','8d431c96-9e2f-4249-8b0a-d875e3273908','b346c1ab-d671-4510-8df6-db1267697ae1','575c5097-521d-47ef-908b-cc659ff249f4','9938a2fd-d07f-45c9-8dc3-f5b88258410d','9d805d19-e529-4142-91a3-155c24c16bb2','3e1c846d-b023-4478-bdd7-f710ed254f8a','21a371d0-9a1a-4d8b-a91d-e3333197b3e7','f49dd893-1e91-4ce6-9aa7-e1047ffee557','b2b5f706-2758-4b90-90a1-c62764786cdf','bafa5083-8081-42f8-9201-04c511f45098','ba6b6f13-c55b-48bb-9264-a3ef3e82fa2a','4d05b629-7870-4bea-ad52-37a43d2b7e37','98333cb6-6c15-4add-aa0e-b322bf1500ba','7ba1771d-f5b3-49cc-af23-5131379a6b2e','5ea86452-f10d-4820-b75e-f710c9d8593a','14ce1096-aca6-4342-b31c-bb7056a00382','0c7bd9e3-ded7-4de4-99ec-d5145361ff48','c609ab21-6794-4f72-a19d-91d2e6f3ae5c','605b7dae-8645-482b-b9ed-19e6e0edd5f1','a645735e-30e2-40f7-9c8c-4b0755cfed79','b0694431-3b93-4bdc-ab1f-f109ea43fcc0','eab11cae-2961-4c95-b2c4-1fff228c639a','c8bdeeef-3c89-41b5-aa2e-2778976cc3cd','a5f69bb0-d405-451b-a249-178482c01fa6','f0aba469-fb2f-42a1-86f8-cbed1d9201df','e170dbd1-a67f-4514-841c-5296b290ca90','8ea4d86b-7030-4b11-a558-2b0e0ef3c49a','c7f97c25-a449-47f7-9eaf-56e41b1ac266','73686819-c664-4ae6-9bc2-5e5f120cbd3d','43a2e77a-5ad9-40b1-bc62-7a964ffa3210','3e58d2f8-36b0-4856-9169-a65e127eb5ba','4fb3e6d6-67b7-4b1d-8846-407d4fbf8ce3','ee7c2f66-60d2-4503-80d2-97d65eba01eb','e79ec95a-a90f-4f99-819c-8e4ec58e6bd3','ab48f1c2-7964-40ce-9274-b5ed65060424','638165c0-21d4-4d8e-9c35-b9dbb2a97095','b1be668f-c194-484c-a7fc-adeb5142ec1a','5f4ee9ad-6c14-4077-8ddc-62e25c09b3df','ccdb1c44-3836-48b0-b9e9-6e180bcaa637','a85dfdfc-345c-4b02-ba1e-140ca992b662','95ad2dbd-a847-4ef6-8b86-1fa38d94e5fc','f659f688-0eeb-4e33-9e86-856733977b42','1887b92f-e532-42da-ab9a-f945cf1c51f1','5a103514-217f-4c0a-a66c-75913c09dd4e','2f5a2012-7ac7-4ebf-9b72-409b29a3959f','f3c29b0c-294b-41cd-a64c-4ab3c423210c','6f45a039-0571-4735-bac2-5f20583e54ca','51109185-ab25-4c50-bd7e-31fca996ecfe','3f754072-f6af-42ae-812c-22830062b341','2fdc8f80-3f12-482e-ac28-8683d448e881','e373b7c1-aaf0-4398-9c5b-43b96d721d47','ebd9c591-3b08-4ebb-9bdb-b9a6eccc7849','5adecf23-248c-41b6-b195-3bb46862bb4d','14bb4067-7350-451c-8c36-c2c199f04d9e','7e34ea34-f762-11e1-a439-00145eb45e9a','2f401916-4925-4176-8d60-f436325d137d','891af376-b9b7-4547-b17d-e1d2e6b8d96b','f8510fe7-fd72-44ce-adb5-c2fed5db3f8e','d6ede82a-680c-4c03-bd2c-0e3f736fb2fe','7afb26e9-aad6-47cb-a5bf-de49dc7597a4','599ef018-1bbc-48fb-ac5c-e7e58ae29a7e','bd09b03d-6bb7-4ab5-a2a8-799a0d132e16','eb95d204-6391-4b03-9602-7dfdfffd4f49','0360f9fc-bf9b-43b2-8c7f-d09e853fc721','42072ec4-b20f-4550-869b-746786fe87b1','902c8fe7-8f38-45b0-854e-c324fed36303','a6a119bb-abfd-4a94-811c-2a4f0f3ab7e2','a02e4f7e-7450-42a2-8fc3-889672d6832e','056e7790-1313-45bf-b14b-1f8b16b574ca','39131221-61c0-417e-a0c6-dc00745917a7','7b828d22-ab17-4f6a-b6b6-7b7ff8c32ea4','50313b08-dc39-493b-bdb4-313aa337a33e','4436b62c-8d2e-4ad6-826e-06672897b89e','4cdba584-5fe8-4d03-8565-64d9cc7ca5a0','f5c7b4f4-e072-4f88-adb5-fb6329a7a5eb','ed0d5a20-12e1-49e9-8207-ec4da410aced','3102b3ed-40e0-4e26-98b6-52c1569d9a62','58f8b744-6609-4c1e-86c1-b6d9a26ea80d','514dc3dd-4723-48a6-a219-8a9ea062a537','ae1b71d4-be5e-41e7-a886-b227762e50b8',
           '35cfb386-7bd4-40a8-ba95-813b5f827671','a3846a81-c16c-40ad-a223-7dbb1caadfe2','6fc68a6b-2c50-4b07-9d3f-f4c06fac3d9a','c761f6ee-936f-40df-bc2a-d9084267bb7a','841c4ae6-c6eb-458a-bf6a-c42d0f7445ca','481fd878-0284-4dd4-86a0-86b0e3d02cbd','336e3eb6-0ed7-46a7-8a13-1faec0d3f8f2','d27fe7f2-0f22-41cb-95d0-1c0acc58887e','fce64d7a-1a84-4b91-84fd-4da5b2e9a946','25a7f866-6262-41f9-a5e5-c44829ea7c3e','11e9ef77-3328-4d5f-985d-4a6d30b307b8','f2e0dd25-5b04-4a90-bc86-3144659d5574','c489091a-75f6-4c51-990e-424d111955ca','b941d3d1-964e-47dc-a3e7-f8edb144e051','17a665f3-f6fa-4a01-bc9c-72bcee86f4f8','320d73ed-133a-4c9b-8b02-e75d77662804','df9dcbc9-f3d1-40e2-9011-02babb0d98f6','b3bffc0a-5c20-466a-b32f-082cf4dd0ec0','cc2322e2-1a56-4ca3-9d4f-4eee808a1707','a4542b83-ed0d-4b2b-8629-caa50849b895','acbb4fb4-94b9-4eff-9659-03fce17bbc72','e16a9392-b28a-47e9-a92a-f20c240f39a4','6bc7c67e-11b6-4980-8c7b-ba5e1d45c1dd','2b93481f-3277-4305-ab73-f17fe29b430f','1b2b7fb8-f28b-4335-bdb5-bfb431d68729','ab663bb6-f94f-4d13-9bab-81316ed1f4a3','909cc61e-2cb6-4f7e-ba5a-ba9a9a3da1d5','84c24d06-3fd2-4988-892e-c79685d14bfa','0777230d-c252-4f99-9c16-cc63c09dfd52','93f335ef-bb92-42f3-80ac-ec7e418c273a','9efee1a1-6181-47c1-887a-278b1fadbcb5','e1231835-c951-4ebc-a3bf-17bffd7692f1','c28aed67-1d46-471c-bad1-e875d5515b59','07692b6f-8209-41c2-803b-31616faec849','a9d21eba-49ae-47a4-adb3-b5733742935e','38af3807-d635-479d-a607-c813931be6ac','e1cdaba9-2a54-4558-a161-cac9c22287f1','9beef55a-b4a4-4031-a1e0-0d2bdeea2c21','a1c36973-1f88-414c-84f3-6e67069b98eb','081b21bf-b603-4622-a7ce-afbcdb25ae5e','d6dd30e2-a04f-4382-a78e-b0ff93cb63b1','d5a07901-27f3-4100-99fb-e393097f6233','d0cd9036-dabd-4b2c-a7f8-7bb8a92bce75','777ef3cd-2dcd-4e22-89d8-d548adaa7acf','75d5124d-b545-4309-851c-2f49c9837b18','5c7bf05c-2890-48e8-9b65-a6060cb75d6d','278feab4-2bb0-4f76-8754-fef92d0cb1f1','a44859c6-af4f-4a2a-a184-1b2d68c82099','9ad675c5-1182-4b25-bb2a-4acc5f51ea16','e1e131bc-b21e-4427-b59c-bd9f5ff8faae','28835237-0876-4af5-b6b6-fb9c1945cee7','85f38230-f762-11e1-a439-00145eb45e9a','954f6aaa-c2e9-41e4-81ca-04eb31912fef','6c03c4e1-63ee-41d5-b7e1-99409f72a6f7','ee71be2d-16e5-460d-967c-9f4602417fd4','f86af1b5-257b-49c5-9ce9-9f1f986a4eb3','87dd5588-18e1-437f-a291-cf7ef9f7db17','f8582bf9-e1e3-4b33-9539-7112937aab63','c05b97bc-e172-40e9-9d42-9df0f93a6e65','3779d91b-a2e2-4957-8e8a-01f8ee1c38dd','b6ed8334-ce03-479f-98e8-ed2a20b0bf98','23efa703-6ecd-447c-9309-193c2e021770','be90e2b4-9c55-478d-983b-47c206ac9faa','e11d99cb-4a96-4e9d-847e-d078cfd59f6c','cc2fa2ed-c65c-487f-91c4-e0b34d6d949d','f5617d90-84bd-4f8e-8b5d-b8b816e065c8','0963db57-6049-4097-96e4-f94f484f9323','a1ca690a-d28f-44b9-bc60-9366d22ab72a','d97804e3-6777-42b8-9389-494e6e4a5572','270dc28f-e919-4755-bebe-89346d297e16','a19133e2-d381-4de8-a7e7-94f47fe90132','9b619ff5-188c-435e-9328-8d819236ac51','c95bffff-560d-46f9-bc64-413607432c41','190be3b4-e7fd-45b0-a6ba-c593eb688782','abde2d9d-94ad-49cb-8186-ec49defb045e','957c25e8-d52d-4b38-b400-aea0ef729c0c','4b8c707f-d006-45a6-be88-c584ec90ee66','b687e282-a7b7-42ca-b9a7-1d46983a42e5','63f758ec-cb11-4292-881c-be3a0d11f93b','dffe30bd-5871-4044-b5fe-d20fee674573','4fa0d552-42a3-42f7-bfd3-789289a850c2','95171a94-f716-4ae3-91db-5de4c0d2cece','639e7857-14e9-4cc8-98c9-7af17484116f','21afc06a-f097-47bd-b85e-ff2301436101','a3f7d0d8-d9e1-42ae-b1f7-d1fc445b931d','3a01c0ce-5046-4792-9f9f-5f413969cdf4','e4fd8292-95cb-4f49-a639-e59c89e82045','29e78377-34c3-4c91-8062-550069a92b70','963a950d-05b7-4fa9-b527-d5234da39f5c','3cd7753a-8724-4633-a147-ef4d50d35880','6fea7d62-3711-4ccc-af77-7e072a699757','94fca048-287c-49ea-8876-34a011ee0029','0574c39e-da5f-4ec9-8987-13841737eb44','e68a878d-ea9c-45d9-a4c6-776ebc101374','cc9fbdfd-9211-494c-b36e-dbd446c70b01','8c3ff4d6-9230-4ea3-b6c7-2940093961f9','e7a2f416-fea5-41bb-8f17-5217fcaa74d7','dbbd61e7-6e0e-4b18-b0a3-f836d55aac7c','5e8bab95-57f4-47b2-8ff2-e65e09ea6743','767212b5-6535-4f84-9844-bce20b7ab44e','fd9b0081-6770-4fea-a6f1-f0c3e0448940','f35e8bd6-f9fa-45b5-b78c-981bc13cb452','00ad9524-ba7f-4450-977e-1563713924f4','b351644a-f000-4e4f-a8d7-f5275ce02721','36ceb840-3011-4411-8739-1a0f02272489','3412de46-ed80-42c1-9e7b-42a1e040e66e','b73e7171-f1de-47a6-8331-843ed8b541bb','31e723a0-57a9-416f-a704-5f9ad27fd5b6','678aa986-0481-4e46-b17f-c371195c7c74','2a69b0d9-546d-4953-917e-7e6e30731a44','bd484fc9-1d70-474e-b019-0a6cb32c19dc','c24d731e-0479-4ab4-b334-db521d5e56fb','b9d89ed1-6502-4d32-94af-a828c11048f0','8fb86698-1f25-4518-b534-aa391af25924','abf09c39-7e71-4d6c-9787-052c2d3e2842','3fd69215-7a36-4522-bad9-85460a64d44f','9013d641-a7e7-47b4-8d07-07ac9237ec99','2b21ecb8-4ffd-4219-a2ed-8314d700d6a5',
           'b7ce62f1-8e9d-467b-8889-af1a2158321a','052596c5-d27d-4c4f-a211-64c0f54d58a1','94d4af26-7196-4476-9d6d-8f9db1a77ea3','caa4bc26-f3d6-4b03-95e2-643609b00500','007f5508-4bed-4101-b7a6-dfd86c52b31d','76ea8695-11af-415b-ac34-d3537b2a0d12','adb0abac-e771-4f85-9914-b4a8b16ad74a','acd76923-54da-4799-b4b0-cfe585c2c0b8','650c9173-80c4-4583-ac81-97ee14f76590','55840438-de12-416d-bf81-d7c8c58e4547','3e9c9135-2f82-42f3-8983-9f9dfa27cac1','892a2c22-d234-4e74-a3b7-d1fb82fc731b','0fb60850-97c7-403c-8293-4efd6ac981c4','ed467fbb-664b-49b7-8d5f-911b9eb5c55a','269bd204-ddc4-4e76-8bff-996fd5f2dbad','57b0a989-1e6b-4b49-ab8a-8aed98b98ef0','f8b3dfc3-e0d9-4173-a63b-436aedce0469','ebed02c3-302d-49ed-b583-b26214d74046','39371f82-72b4-449c-b39b-7d5c2c568d48','9a343474-037b-43c3-ba7e-1ae3622c2908','51408b36-de1a-4b52-91af-4052d1a64932','59361789-d4da-4bea-b672-4d27cd6b12c2','f875121b-07ae-4b44-a928-9fb793874d54','e85170ef-0fe5-4a50-86a1-4d8551ae581e','486a6494-33f2-4f8a-8498-b31f39b66ac1','82abf189-6d5a-4426-babf-4c2074aea90e','06ff6625-79cd-4030-bf12-3b251e93d1bf','c379500a-39f0-4f69-99d0-b586516f635e','bdee10a6-b34e-4795-b17a-94c467de28ff','55600309-1695-4595-9ec2-90be6e6fe506','b9d65394-1c8d-4df9-8d45-b807af99889d','6cb80484-b9cd-4e83-b81e-70416f61f5ed','0097a2e6-0eaa-4cb0-ad6b-ff2065a0e35c','c5f1ca2b-da1a-468a-9b85-f690ef0d4a81','00156ffd-cd63-464e-9d7e-c597e477b6c6','a60aa653-c01d-4e7a-b107-c92205633e93','474eb947-606d-4e86-99df-800af617e6e4','8e08523b-4f29-4cb7-b4c4-ff673ee09b9b','fa2c5df8-8f1d-48e0-9bb1-d4083f1c8596','76f4128f-b941-425e-9f38-24035703c47b','95a410f0-386b-4792-8e5d-ba2cbeecfbde','37e97070-1d18-4cc8-a004-0add44cebbe2','47d4d065-3486-441e-a70b-707eef444998','6a70015f-2d0a-45af-8ae9-a2e53d453b55','85f9137e-8aec-4e0b-9ed6-0af4dbe491e8','f412ff44-1b43-4ca1-8e10-86b34cd82da5','89e22f48-ea07-48d3-9c41-bad6a6d4c934','4dc3f35e-eb7e-4f73-a12a-a51a6f525002','89b487bc-6b66-482c-a087-1393d1edec9e','591a3831-a732-4047-a322-38503c4dc69d','e0507994-aa35-4ec0-be28-92d4a3c11f75','4f6a518f-3a43-41a8-8989-af0c4eb288d5','d2c8bf26-2179-447d-b1a2-3df7f9253d87','def5a43e-0e85-4789-9c0a-35c23ac90879','58fb122e-a1af-4a99-89bc-1d03523c0d8e','18e4ee37-4737-477a-a1df-6840e1ad4553','4d2693ea-6151-49aa-98f8-6bf5e1409f78','52a921c2-83ea-450f-95f2-5a6bd5c9093a','d922b606-6c94-4d51-9277-36c9b03872a7','e4ed7202-d694-4912-ba7f-93a206a249c7','31bb628c-cc7f-423c-914e-746271fb5694','1b64016a-cf65-439b-bd43-4ad75f66b37c','38f2594c-d424-4ac3-a560-a69bfeb6dc3b','281d50e6-3990-4a02-83b1-a6ca3330ee97','b1ffa78a-30c3-49c1-bc6c-4f7187791a7d','5d324121-3c3c-429b-85f5-5f61a967d8c0','7b8ef914-da91-4ea9-a974-57a03144c7f7','fe509a1b-3f0f-445b-8332-1d6d9ee9e2cd','e9ea0fc7-1924-4bda-a9ea-b3a5a6930ecf',
           '2d684bb5-ea11-4709-ae12-8fc0a800287f','63e504cb-59ea-4043-b390-a4639f9c71c6','7648036d-fdac-4ebe-8861-9a28134adae1','dc383f1f-6456-40bd-9ef1-0780cdb0c66d','22c3be28-e74f-40b9-aeb5-c427fdee496e','0ede0c42-61c1-44d2-b689-603848bbe219','31f8727c-debb-4c38-bb89-0eb2594537a9','6937281d-4953-48d0-bce2-03debeb48709','b086427c-bf5b-49a4-8bf9-20aee512af41','81a55a32-e89b-4959-8e49-0481c4d31973','44f32d6c-0354-471d-b17e-4ec84834e2f1','90c3e206-75fa-4527-9e8f-9406af78452f','2b4f6d66-d958-4107-a6fa-3ed6ada9a2f6','74ca3dcc-32f9-4981-a3b5-dab8c6a6457f','267b8d33-02ac-4fa7-9fb3-13fdcd330015','b0de8b15-fb55-403c-8b16-d58929390e7b','3c273f73-9fc0-4cc7-906a-d05614b6aa40','9192a5a8-5eba-4ec6-a336-797924214175','eb5d794f-e05e-4d96-b173-363bd3a1822d','20e2524f-0354-4090-ab7e-c8d7c3e953db','95f572da-a3a9-4706-bccb-03521079a520','4bb083e8-53b9-418e-b83d-105e75a1798d','19979096-dada-4247-a5f9-92601a933221','a7f3a2ac-fb04-4a97-969c-3bcf78a7433c','42a55f11-4aeb-46cd-b7e0-b6cff2eef92b','63756d9e-8701-4b86-9467-071d7228b2b9','8dbc2707-eae6-40de-85bf-0625f9f0a10b','eb0ebe4c-46e2-4996-b0ec-f92ba783165f','7f0a89f6-46d2-4312-ac6e-f02278c4f1f7','2bbdfd35-4881-4ce2-a0e5-6d457f01f3cc','1bd56795-0669-4e5b-a3a4-41527fc4e66c','307ddcff-6195-4f43-8f49-515ccca112a7','447eabf9-3b04-4927-9420-52c5e5c096fc','ac48c9ff-e471-476d-b826-9a2cee4caa66','d47f8848-8de8-4e30-bb82-27d32da5ee64','20d66963-96bf-4cfe-99d4-67c00500b891','6043b710-f1a6-48bb-a473-8b32b1e43408','1ac5595a-ed78-46d1-9c1f-624197928f38','0101bbf0-146d-40ed-b32f-b21a64183c47','4071501e-25fd-4a1c-9381-a3d5cb8d166c','ba9b69e2-a26d-49f3-aba4-034d04489b62','8e6bce77-f46b-451c-81dc-f0713ce292c2','994fb34c-ba13-4768-a238-b1d3eb35c90d','677421cf-7213-4f50-a2a0-f47921fb18ca','9b17d0c9-4561-4bb3-a2ce-0cdaecad95bf','38c928d1-ae8b-46fb-a01a-08bd9cb00f73','06a9f1b6-cadc-4617-adb4-32ce7800775b','edd76a7a-64e0-4008-a741-105ecd67e339','4352e0b3-2c1f-42a0-a445-eff75e37cd36','8a7d18a0-2c93-41cb-a018-c14d3ead8a45']

currentdatasetkey = 'x'

def get_cit_for_dataset(uuid):
    cit_url = api + '{}'.format(uuid)
    # print(cit_url)
    response = requests.get(cit_url)
    rson = response.json()
    return rson


for key in keylist:
    currentdatasetkey = key

# kk = keylist[1]
res = get_cit_for_dataset(currentdatasetkey)

print(json.dumps(res, indent=4))

templ = []


def obtain_cit_count_datasetkey_pair(xson, key = currentdatasetkey, term='count'):
    count = xson[term]
    print('¤')
    # print('this is the count {} for {}'.format(count, key) )
    return (key, count)

def driver(lof_keys, finaldict = {}):
    for key in lof_keys:
        xson = get_cit_for_dataset(key)
        pair = obtain_cit_count_datasetkey_pair(xson, key)
        finaldict[pair[0]] = pair[1]
    return finaldict

fin = driver(keylist)
print(fin)

csv_file = 'c:/Temp/dmitry_russia_citations.csv'
with open(csv_file, 'w') as csvfile:
    for key in fin.keys():
        csvfile.write("{}; {}\n".format(key, fin[key]))


    #
    # writer = csv.DictWriter(csvfile, fieldnames=['dataset_key', 'citation_count'])
    # writer.writeheader()
    # for data in fin:
    #     writer.writerow(data)
# fin = obtain_cit_count_datasetkey_pair(res, currentdatasetkey)
# print(fin[0], 'key--', fin[1], ' COUNT')
