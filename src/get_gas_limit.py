#!/usr/bin/python3.7



import requests

from src.inputs import Inputs
from src.setup_log import SetupLogging
from src.settings_set import SettingsSet
from src.send_req import SendRequest

class GetGasLimit(object):
    # http://bin-hex-converter.online-domain-tools.com/

    def __init__(self):
        SetupLogging()
        settings_d = SettingsSet.settings_set(1)  # 0=KathyUbuntu, 1=westteam
        hex = '504b03040a0000080000aa7b564e00000000000000000000000003000400696f2ffeca0000504b03040a0000080000aa7b564e00000000000000000000000008000000696f2f6e756c732f504b03040a0000080000aa7b564e00000000000000000000000011000000696f2f6e756c732f636f6e74726163742f504b03040a0000080000aa7b564e00000000000000000000000017000000696f2f6e756c732f636f6e74726163742f746f6b656e2f504b0304140008080800aa7b564e00000000000000000000000028000000696f2f6e756c732f636f6e74726163742f746f6b656e2f53696d706c65546f6b656e2e636c617373b558f97754e5197eeecc90990c972d9090059209a498cc9291a58a8152020d35ca5602b1605bbd99b9492ecc12670922b46ead4babd56aeb5ad1565bd4aa2c020169d59ed353cfe93fd17f84d3d3e7fdee9d3b37612639d5d31ff2ddf77ecbfb3eeff67c77f2afff7cf639804df87b23a23825c323329c96e14c1831fcb411cdf859108f86119497281e93e171997e22cce149197e1ec62ff0d462acc2d3413c13c672fc2a8ce7f0bcccfc3a8817827831cc53bf91e125195e96e5df8af4bb205e09a3430e44f19a0cafcbf086a87d5386df87f096cc9c9597b7457a27843fc8f38f21bc2b7ade0be24f41fc39887341bcaf219033b2a686a6bdc78d692399317213c99152c1ca4d6cd3d0503c951dcb673484d266caca1a99a2066d58c3e252be646446ca535399531a5aeca359a33499dc654d0ce74ae68459e0f1d098417d2993a796d97bca252b93dc674c71b171c49ac819a57281c68766af6edf6be593b972a6984ce573a582912a258be913c9c174ba60168bdb6a9bdb419d412393c99f34d31a4a5f43e337342f0056f5f6d58a6360773e6d4a10ac9cb9bf9c1d330b878db18c8a7a3e6564468d8225efce64a0346931643db7c228e54f98b9e488959de26691a9bbed503957b2b2e6a855b4787c3097636e4a563e47151b6a7b62b87b92a39679924afcbd7d4c6b6b05fdada96cd86ee5acd20e0d3b7a6f75b0decc5c35c37da31a968822cbc80c66f304ae61dd6cfc078d02ebb164166639125dd09143e64365ab60a6a5b2541548e16938dcbb4032e75dad1b8e45f99339b3a0a173fef3acc8e294994bcb565d1d19ac14e8a269235336a5796655c0a9a94a152c192919a9132c47f56eb302b5d048ae386e16f614f2590d47be917bb5bdeb3bc6121c57ea7da53cc3e974f181710d772c60af6ec0828e129242c5030d772e84be2ebea0313555c84f53dd722b972a9846d11c543306c92a6ca4d3667ad48eef7232d79cf565c5f29832e66e0ae53315510ebb49fabf84973d1032ec2d1babe2260f2ed77eb868565f96550e559739b3ab12d7af19cc5109a6bdc583c0d5ba283569a64e90657aeb9f4fd659ab7fa24115ffc68a40df63f3eaf0528b9cf7678b131a06ff27bbb5358547f2e542cadc6349cb2df7306bbf6cd7d18fa48edb65d8884d3a36638b8e217ca0e3436cd1b0a27a6fdc6d1427d9ac3abe8d3b74dc25c35f64f347f858c727381fc4051d177149c7a7b84c42abc3edca76cf61a74586a64da1c82573def5e11ca96477c62816cda2e0213d5cd17115333aaee13a0fccbacf782dd58a888e49983a72c8e83821c367b8a1c382b910ba4a2755d0cd7ad79116adf7e05e1d79301e7fc5df747c8ef31a3a8673c5f2f8b895b2b82fe274703aa254cbe6691d5fe0bc8ea36087270e4f9a11551d916cb9588a8c999109f6312f864869d2c845f2850819dfc8f078e4f67e394e289db32c389413c98fdb36fac5c52f79e32c7cafb216aae57260ecb899a2f6b535fb6bb7f3a261cd7c5153772c0b2e706ce8d001be1c1edacf712a7f527a6bb82e6f86b2e54cc9529f59fdf55ab0ded9d69a78f749eb34149d5b29c22b7f812bcc3f55a6735bbdf7be1d916db7cef4dd3aa5a1bda68123ac4e524ec0cc5a54df5587bd544dd93d3f6172df861a306a1a0d16ec0f025ae83d26e71b53f9ec9451607ee761337e04f9c9868c7b85097943f71eabc51de8e637750c3ec49140039a842af8e3a049d8423d49187cfa8433d493c400d2b492b7f2ef2ecffb003fd699616ca3bc9d3349be697c2e8a5e8676416df90ec70635b9163b38eaf6067c173bf91c745677f1a911422d45beb98ad62fa8682376d750e4ff688ea2be05156dc6f76a280acc45945c50d110f6388afecd1d8bf834a3335476090d571088de40f0e80c4257d05815c3d1d81568d1f815f8a2cd812bf0471397b0b8397015fa552c915397d1780d4b05d0752cf3e3be1b587e54736666b0e21a9a2eba40fbb158fd060c30658bb11a2d6865296cc606a639c6246f645a0799d6434c729a491687b6d8401d8744ea57711049cac5a7a4ef739f5f491b95febb29b705b86d58797eeb4892e50189c51754212692441c8e5dc74a1fbec4aafd89af1064602e24e2ce54f340a02df015429c1449c21f505e75f2f72a887529313611650bc3bd8ec9bf8d798b33e4552f92ae1749ecc53e276dfb29f978ba1b07e8bf9f6797e0204f04f00327a1f6da56ae1de2cc52f86ea22588919b680ee2f0ac248bdf4b7c737c3d825127ef670823c0674f34c6142566d0128d715c1d8d736c95d4c54492ac05aa85daa2c0df8b46825e46b0cd84bc8e80c4b1a8adcf75ac07f7398ef5e087ca31910eaaf408b895fe9ae9e0bde5a4e3491e914cf6c4fe8960e01c02fe6b68932aaba4a6795fdc4ecdbeb8e4c0ef817884d11a453b2174d2f83aea1488115b9f07a21dfb7684713f81f9545417c31fdaa9dd446bad90063517e98ff0632798166d8ae6ae2863199728c6e24e143921f29c3836a9583d80101e64120d92d1980760970bb04b454e53d24105b0665a7fe22279d041d21e750cb7df404705c49ad92096aa9d134ce624bbcff200687701b4ab9ad494340f80075c00136c0151d15d01b0b602404d5c45671d1c59e2c8d1cdbc0747b78ba3dbc5d14d1febe2305c1c978943623c142586ae8aedfdf1c45544ce62859a60e53040e7a057b0b6cc83d5efe9f022a35c22ee32ab6d9a55f4302faf47d8e7a73d8d30e4621f72b10f31cd5b5487df89946a04a9b746e9e21e165ba896533ef914a42c4e3de1907584f545740381685b40bc4bc8108bb705e85d375daaf2acdd0d8fb2d01ea3d5c7b1923abad85955268ab83823187770469846bb61234ec3865821f72826f2c907af83e78c83a7d38327d1b46e06eb2b687a66a1b1cbfe296a7b1a2bf00ccbfe590f924e1749a78ba4d345d2e922697191582e927f7045740cd8b1f0f2b74dd66dce453610508b6dce1dd51688276c49507a59fc39ea7b5efe958836bc40067991fcfc126fa2973d88075cc4032ee20117f1808378156fb5e3e4f32a8bdb335b3923f90f816493248bf3147f42381e9de6aa448ba1bc8a6fed8fc69b36cce0b68a7b8db10423de5d85ee4df72b64ac577975bcc680bf4ee86f78ca72bd0b793d5b6e9ff30563b776031372bf82ec931f340e90a203a4cb01928837f54a862b207ae682b0b3fc16d59d65cdbdcd78bee301e025b7ec1c726b60ac2b00f8b3c701708c6f12cfd5bc075648d3b285dfacde0817dde60cab6def320aef29832df631d7e06a654653415f045fd34e4dd979c8b133e5dc371dd19804597843cabab62ddbc973d4f33eed7e407afcd0435c1daecd0e14944d918aee1543eb2d8ef59263dd74acb7d6f0327e0d7d73ddfc98ee7ce231d9ea9a6c75dc14a9acbe8be6383ced96984f79b1a68ec38959666d8f2f52d12542f894fe5cf6a4758d6b7e8debf11ac7639104887fb6ef2755c53c8c5f2ae53e2c278b3e4b36ece0f35534fe17504b0708ec308779cb09000028180000504b0304140008080800aa7b564e00000000000000000000000022000000696f2f6e756c732f636f6e74726163742f746f6b656e2f546f6b656e2e636c617373a552d14e1341143d03b5cb16aa28a8a0284a08697970131ff481a76a24694282a19507dfa6bb431d989da933b325fc9a0f7e801f65bc534ba5b6a5896eb23b3be79e7bcebd33f7c7cf6fdf01bcc64e84e711b623bc60a8367a3d6bfa5c7de80bed19569a5a0bfb5e71e7848bf092186dcbb53b1376c828699e0b86f55afde89cf779a2b8ee262d6fa5ee1e306c9e14dacb5c9c4a273b4a34b4369e7b69b463d83b9226d18572496ab4b73cf589cb2e123ee224a7525c9248d95de51da318963291ca9c2b4a5eacd59b0ccb9ea8aa55f47aea8a61e3ba869cfb2fc93bd96d6a2fbac29244dce154582a8ecf18ded4a61b37b2cc0ae70e668aec8c37f3915b6add0b3bd6d5fedcae4ec4d7425a9191e2921f1e26c3db39554d2faafe99eee85ae4d09a9ce1d33ca17fb489f86034e8ae63ae94b90cc7c9d0fe2fb799475d6999c2a6e2502af2a8b4cd85d0af0295616b42d0876832e030acfe19c2e3ceb9486942f76fcbd8fd6be06f278fcd7e99816101e1894b749788695fa15d99d66580b0952958157727b07b589dc0eee301a9dfc0b0466f144cd70784877844ff01ac2efc0647a1c7d81886d6166f864684cdd9b94ff0748aef388d085b83ef33dca135141a7c4ad46e488a10ff02504b070868fe421cca0100005e040000504b0304140008080800aa7b564e00000000000000000000000030000000696f2f6e756c732f636f6e74726163742f746f6b656e2f546f6b656e24417070726f76616c4576656e742e636c6173738d565b6f1b4514fec6bbde75b69bbb49d224b46929e05b6a2ee19a4b73218140d2943835b4406163af926d9cdd74771d90a0129540ea033c801020242e2f252f790089b80824c45390f82ffc03049c995dbb89e3243cf8ccd93367e67cdf7c6746fef39f5f7e03f018ae6988e34213148c7333c1cd248f4da998d63083e735bcc0cd0c66b937abe2450d2770218697f838c7cd7c0c176358e0ee256e5e56b1a822c71075deb64d97e1d49ce564ed72c9cb161cdb778d829ff58a6bd98962d1353d6f9841f5364cbbc853a39b46a96c3274cd5d37368decbae1af6627ad9559db37574c97529511cbb6fc3186cb89a3773d66b6e1f6c93c833ce5140940eb9c659b17cbebcba6bb642c9728d231e7148c52de702dfe1d06657fd5f2189a2736365c87b04f6f9ab6cfa0cfdac47caa64789e49d39983607c67cdb4b34bdc9edbb798389e5d2cdbbeb56ee62dcfa22a970cd758377dd39db06dc7377ccbb169cf546382462d27bb68de285bae59a41d632ba6bf10883190481e2747ccab659f39e694f98969b479ae2aa0e6edf9e065f381a03d54f6104979b930eb64e2706114a2639488f97d6152c9b057b20bcbd7cd823f9cbccac01c2ed28129219241a234e77ca3b0366f6c08eda8c1a9f4aae1ad06824b89e42c152156e5122533fa88f94ece772d7b85215e852f760ea2b4b39673ca6ec19cb1782f6842cdf33c4d471f967474a15b470f3727d1abe332f22a5e21e9fe7f37a87855c7237854c5151d4fe16986ee7a189365ab244e3bbe6fe5bbe2f28deab88ad7b8799d006606c28b364ae43203e2ae898c37740c6384a1adfef4187a1bea1ff6391d5a3e9059f43a43e7be7312413aa6fea308379aded362c4ab514b9054c60627c330983828cd41b5c2631aaecbaff6cf11f9fd89a9c3a771869ecc38a82b2121c215a78735c2451723e94ea346f37de8a7effbe9ab44a34c633c75172c95de412495d981941adc81fca358758a6c17a2646f50a68b267868818f4e94719aa2a9603d06f000203c5e97098f578e088fd796708efc4e89261f2467bf7d080f93e590b234f2e5d1d44f88fc50c3a088e03ba2a61e248435191248868bc7289b575404977b0c34117d8fd6dc143b74055935d44a889a2e444320523d90f71b0249370622d503f980d67c7808909e104806830d80c8f5406e3704725e2c3a0044ae07f211adf9f810205c335e98ae7cb8d75f9423d1782b95fe1e51793bbd8b965405d134fdee202a6da77f8732cf75dba58ea22143bf0ad4afd0ba45375ec4298b9f679020514cda9b205513e45db4f381627205b12db472ef0fa8f21664699b404882462f01053e818a4fe9e43e23989f13e52ff026be14b40602c0355ab7e89fc6e3824e1143148be009d1a0badac2fe46bf8a2715d6adb0b836cea9d32b1752ff393cc6e9805d734a306be26046da4ef7ad069c78580ac36f55e37210271a5a10efbb07bf43dc9eafe9367d43cdf32da6f0dd1e35a643d89d04fa193c4b5038d84128ede3ec5fbae511824b30c947e84718cbefffa445f49c862caed1b6bc51867ec5892b77a1773457484141a5b5a32df025eeb7073e616e6dbb594147059df58d77674fe30d8540231815760c67c3a746c173f42c35fd07504b0708ea7bbc798f040000e6090000504b0304140008080800aa7b564e00000000000000000000000030000000696f2f6e756c732f636f6e74726163742f746f6b656e2f546f6b656e245472616e736665724576656e742e636c6173738d56df531b5514fe6e76b31bb60be19740015b5aab8624b06ad156c36f84160da5051a0bd5da25d9c296b08bbb1b5e1c1ffa6ff8aebcf0a033923a3ae3f88433fe2ffe078e7aeedd854212c0879c7bf6dc73eef9cef9cebd933ffff9e53700efe189864e4c3441c12417535c4c73db8c8a590d73b8a3e12e177398e7dabc8a4f345cc244029ff235cfc54202f71258e4ea7d2e1ea85852b1cc203ff3dc6d862b79db359c4ad9378aae1378663130fcd29631552a7996efe7186281cb10df35cb158ba12bffdcdc358d6d33d834a6ed8d7927b0362c8fbc9451dbb183718687a9f30fbc60b7e1f18305823be3960840326f3bd6bdcaf6bae5ad98eb65b2b4e7dda2592e989ecdbf23a31c6cda3e43f38a673afe33cb9bddb59c80419f771ccb9b299bbe6fd176b61e4ce06e598eb1c2e58d53c154e3f5a58a13d8db56c1f66dca72dff4cc6d2bb0bc29c7710333b05d87ce4c372ed03cf63196acaf2ab66795e84475c30ae6040d03a9c18b8850fd23e76b17f498f72b4e47af70e6fc704dd0772124b187729d4163c23ff6ba9c3a9b0c854a30cb54ed6b9153d974368cc5f5e75631c80dae3130971353b72588318988e6e5c02c6e2d983b822f1a674abd69fa9b21c9526a709e92502d95323933fa4804ee72e0d9ce0643e7117c717268a593b565b7e215ad399bf3af090687b99b8e3eace8e842b78e1e2e2ea357c74314547c4674fdff0950f148c73b7857c5aa8e5bb8cdd05d0b63ba62974b96c7d0712af26b7ed5c674ace131179f132bd981c01da3b2b203e26689cd2f74e430cad05adb3786de867c47534ded2a84048bc9a6eca73a248cd4a0fef34a6db47d62a4a8eb8d8681483277762ca7c43094aa27a59ea7a841b91affa3c939c7bf3f3573f636aed1d3d8099a47488871aee9018d71bac54a8cd3aad17e1ffae9fb75fa2ad32ad3da997e0996ce1c2096ce1e404a0f1d40fe51445d21d98538c92c790ea109c36881810e1a82ab644d87f118c01b80d0785e26349e3926349e5bc20dd293120986374fc8b7f036490ec7a09587c6d33f21f6c3717e45186f8a7c7ae810e5634861300a1e276f9e4d1175bc42af09eb2d8ab92d4ee80abd8e112b1162ba060d8148b540720d81641a03916a814c50cce419407a2220596a743d10b916c84c4320c322a80e885c0be40ec5dc3d0308e78b27a68b1e9df517f970ea5ea433df232eef670ed192ae229ea1df77884bfb99dfa12c70de0e699a68c9d2af0af55b24f7a065859dbc783f4307896cd24907e9c8413e441b5fc8265791d843926b7f4095f7204bfb04421265f41250200f150bd4b94582f9804a5ec2975816650d84808fcb7a41ff266e8a724a18215b0cef8be1d4d516f637fa557ca0b06e85756a93bc747adba2d27f8eda381b56d79c1695357130a3ad57fb36c39ab8598acc4f8fec7268a732b4d0def70a7ebbb8398fe826add2f0ac119b8f4fb0311bc1ee20d01fe22382c2c10e41699b64ffd20d8f115c82493a223dc658e1f42705d1531a55f1848ee58332f22b2eadbe84dede5c25064529c9f6d65097b8de16ea8439d9fa4d15ed5574d40eded313833712018d614cc8715c8f9e19051fd393d4f41f504b0708826261e37e040000ca090000504b01020a000a0000080000aa7b564e000000000000000000000000030004000000000000000000000000000000696f2ffeca0000504b01020a000a0000080000aa7b564e000000000000000000000000080000000000000000000000000025000000696f2f6e756c732f504b01020a000a0000080000aa7b564e00000000000000000000000011000000000000000000000000004b000000696f2f6e756c732f636f6e74726163742f504b01020a000a0000080000aa7b564e00000000000000000000000017000000000000000000000000007a000000696f2f6e756c732f636f6e74726163742f746f6b656e2f504b01021400140008080800aa7b564eec308779cb090000281800002800000000000000000000000000af000000696f2f6e756c732f636f6e74726163742f746f6b656e2f53696d706c65546f6b656e2e636c617373504b01021400140008080800aa7b564e68fe421cca0100005e0400002200000000000000000000000000d00a0000696f2f6e756c732f636f6e74726163742f746f6b656e2f546f6b656e2e636c617373504b01021400140008080800aa7b564eea7bbc798f040000e60900003000000000000000000000000000ea0c0000696f2f6e756c732f636f6e74726163742f746f6b656e2f546f6b656e24417070726f76616c4576656e742e636c617373504b01021400140008080800aa7b564e826261e37e040000ca0900003000000000000000000000000000d7110000696f2f6e756c732f636f6e74726163742f746f6b656e2f546f6b656e245472616e736665724576656e742e636c617373504b0506000000000800080051020000b31600000000';
        self.chainId = settings_d.get('chain')
        self.url = settings_d.get('url')
        self.pw = settings_d.get('pw')

        self.head = dict([("Content-Type", "application/json;charset=UTF-8",)])
        self.req = requests.Request('POST', self.url, headers=self.head)
        self.req.json = {"jsonrpc": "2.0"}
        self.remark = "get balance"
        self.id = 99999
        self.contract_desc = "(String productId, String reviewComments) return LReviewContract$Review;"
        self.args = [["swimsuits"], ["too large"]]
        self.senderk = "TTSETeCA3FWQ3Y32TCFEwJvzqGbxiXNxtkzPb3z"
        self.contractAddressk = "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM"

    def send_request(self, req):
        r = SendRequest.send_request(req)
        return r

    def setup_top(self, method, plist):
        reqr = requests.Request('POST', self.url, headers=self.head)
        reqr.json = {"jsonrpc": "2.0", "method": method, "params": plist, "id": self.id}
        return reqr

    def get_gas_limit(self):   # returns the gas_limit  / "params":[{{chainIdk}},{{senderk}},{{hex2}},[]],
        # hex = '504b03041400080808005455924e00000000000000000000000025000400526576696577436f6e74726163742457726974655265766965774576656e742e636c617373feca00008d94df6fdb5414c7bf37b1e324f39234f4074b37da41a089932e63fcdeda020b1b04da6db463133ce12656eb2d758aed741230241e40e201241ee0618fa0f1432ab049b49340423cf1c0df8410e75c7beee266c083ef8f73cf3de773bfe75efff9f72fbf0138813732c8e3b92c8a38c9a353dccc7133af61218b144ea6f13cf72f70f3621aa7d368f2f025de7346c3cb59bc821637af6a784dc3a24066d3ed75fa6dbfd511282e5e31b7cc46d774d61a2bbe6b3b6ba70472aeb5655bd79abd8d0dcbf13d81d435d7f62d9706febaed958f0b141697431fc777cdb64fbb5273b663fb0b02ad4a7c717f92ff63a95e12509abd8e25905fb41deb5c7f63d5722f9aab5d8bc17b6db37bc9746d9e874685f108ee32e3060c67b6e808027acb712cb7d9353dcf228fa331c2727c079d475fb3fc0b7b4a8d56aac3b4d2bd01afb1caf0738c50b0e598aa23de7e5b86fc2e876267bcbd71daef05d14867eb9dbed9f562b9ceaf5eb148e9ea5b02a23758d77049ca63921607577cb37d75c9dc94aad115a1f0eba6b71e489dac545b94c4b5bc7e979c054db22bbdbedbb6cedaacf10383ca1de33c3a1ec4211d252ce918c5988e716e263026301197e374dfee76f84807a26b383fa3e31cce737381d0ebd383f76f7e8610ead3c11d64df1aca3a5ec7b2861581a9ffa8a4868b3aea98d5f1049ea4bb11d745a064f71a4ebfeb35da618c86d7b9da082f0ec941e54b999b9b9643f59d1d56df7da6f08c24f9e14af3df96d3546e792949d781fb258dfc14074f37c01f04c334fd0d8aa000509060f9e9c791e00ac87e82fb42810b44f32cf9953049ed619ab9b4ae525f326a3b10c61d248cfa0e92c6ec0e14e390b203f5b68c7184da71e9f92e32780f39bc4fd9ae53c40ff010590dca4c513085870139628a841c3147528e9844a1cc8fa01ce66f502fa8578d9f91bc15a54a49e38732b41e3884a1051ec563e1e605f2e61429864fee8166a5f523daf3b18c301e7845702909c7896786822871904f86825486832871904f69cf67f701190f41aa4341d438c8e743418ce1206a1ce40bdaf3e57d402642905a04b2413e9ca7f92b526fde81564cef22c365a2ae30b38b6cf140605022831e18d4bb86c2756a7671307e8c1bf71ca3191d835e6898fa07f2e61bd3326adf4055b66b7f2067ec2257a3ef26d4e476ed77e49798a52e790a37d8c828758913cdd5baa4296c53b0a404281102f015347c4d0fe226d9bea5b4df611edf4ba8e92071a44c0bc764498e10de71b225f0b84457b59cf80ba31a4ee46995fe2b217a27ac4039506a64ae3035b91e8834f2f6dd892a2793db912c45f97c7e441a3f511d6e519edbf7d4a91cd2a429c353789a3225f08cdcfb2c8e864f3a8fb3c49ef807504b07086c47f91fe203000036080000504b03041400080808005455924e0000000000000000000000001b000000526576696577436f6e7472616374245265766965772e636c6173738d955d73db541086df634b96ec288e713eda249416638a2d274df92e891ba0a60143927ea44da10c43155bc42a8e1c24b9bd60f805fc03eee12accd01992cec00cc3552ffa9b1886dd23c5b15575860bafceee39da7df4ee9ef1d37ffff80bc01bf83c0b0d2b394ca3ceabcb6c56d9bccfb10f345cc9a1818fd85cd5b096430e751d1ff3f3131d4d1d9feaf84cc7ba8e0d1d9b1cbea6e1ba4076dfebb5fbada0d91628aedfb71e584b5dcbdd5dda0a3cc7dd5d11d05bbdbd3ddb0d7c81cc43cf096c8f1641c7f1cb17050aeb37ed078efdb0d17303cf6a05743e53775c2758156856e29bcfa6ff3f91eab680d2e8b56d818975c7b537fb7b3bb677cbdae9da8cdc6b59dd6dcb73d88f820ae31149585ec068baaeed35ba96efdb143f15e32a872eb11bbb7670fd448fa94a354911c31f39355d49661ea3648d817663feb097a5bd3b919859ff649db1bfeb5b5d3f96f4dace7d9be4abde1510bdd136455bf4a6177decf85660b5beddb0f6a5183417d4c28ee5774205d3956a531ef6fbdd80d291a307bd905a20b7d5eb7b2d7bcd6115274755bac0450dcc61dec08bb8616006a70c9c6633cbe626b634dc22f2447135dc36b0880b06dec2dbd482b86257fa4eb7cd0ae4bf2f0d26b2b45c32b08d3bc459a2df0201968ea79103cb045f0a6792dd1f0c5cc2791acab83cf2b3a9233a7784a7803e6ea4b5324822e647d947521d6b94b1f6f76d97fabe98d4f76742d187ade01cddd569baca0a522c1dad52ac9e7ccef2b3506071c9cf4190c267c8be449e47fb2a3de7ccda2184f9182973e1106973f1108a39ab1c427d24739c253b234f2e238b15e451c7242e53ee55aa0d985499b2e0659401b9628a945c31475aae9844a1caafe27c547f899e829eaaf93bd2bf0d4a6564f04399da080f44a9055e43257a79954e73890cc3a74f4073327a95de59931966c25303b88c84e3c2d54410250ed24c043193419438c806bdb3f91c90d311482d11448d83dc480459480651e320b7e99dede780cc4620748ba25cbfd2196e5bd3acfd025539a83d41de3c42a646bf9fa1a60f6a7f43dbe0be2dd0ef08fa4f1c64f9c857867c957c95fc034a969638735410b84b33fb2529f0154de3d754f81ecd9325f1ce858507784d52e522619da14f7d9d6229facb6219542d2ffec1948637276897ee7e84de8e64289b922c5b2f9c9def98922a7befd851a5337f3010a92867f81be8d8a5bbd44109ce9058e58846a7dbf30ede95625d1a74ed473ac34db1fe44ee8bc7182b1a47180fab8f17f36c26d814d8bc701c0b8986f78bf17d75b03f49e60853f189708726c28a1053784fda65bc125d788dee5209a9ff00504b0708ace91217c3030000f0070000504b03041400080808005455924e00000000000000000000000014000000526576696577436f6e74726163742e636c6173739557f957135714fe5e162686513641a3288814c366ba58b5805644ac690111148aadd2814c61244ce2cc04a5b5b5b576b7fbaadd37edf24b7b4e8b52cef1f4e7fe49fd41fbbd49800442b527272f6feebbefbeeffbee7d37c9dfb7febc09e07efc12c4360c2b782a080f8657a10e5a1095180960348818f4009e0e620ce30a8c204e61228820e2859884a920a120194411860bb106a7a5d15260075186b8dceb049092c6a900ce14e22ca60bf10c9e95c33905cf29783e884d1896c3f9005e08e045399d90a75f90c34b015c54f0b2825714bc2a503c68198edea74f19fa99ce29dd7404d4a869ea56475cb36ddd1628482f0a28963ba1a9a8eb9436a545528e118f746bc9568155fdc698a939294b17e8ca5d6d4b3fc635732cd2ef588639d69ae5d065d84e5b57fa888e84e958daa8539b7e6cddcb17cf6f334cc3d92be00dd70f08f83a12315d42304cbd273539a25b47b591382da55d89512d3ea059867cce187dceb841c0c54b4e60d8c2338bc405f6845742996da95f0128f927ad442c35ea446312c8b28d026baccccec9498a4c488a168b59bacdd9e62e23113153713b329a891bb1631391f6f4ba54c0caa05cb7e2f9c1b48b5453b2cdd597eb15b9e24c27e705aabfeb5c08acee77b4d109a6d4ddabe035562fcb5520d497321d63521f306c832beda6997034c74898b63c202f3b6dc127d2ab4dcb783ca026374eaf666993baa35b39011bee18b04f3f9d322c3d267519d39dbef9b2adcd93e4a5fc5bf3d7c2ff91a9ee8e0007d2492b26b8f678bc77be7408716db83e5ff5780cd6553099e5987d05fb7509db6b48bbd79277766bee6a9e2b2881d62e2395c7cded15afbb9de50d62e84fa4ac51fda0216ba72c5783ed72b78a7b719f40c962e4439a3dce9a51d18466156fe212ab3143b93a7aa0dab0abad4cbe14bca5e26dbc2350998e5c3d7f5daa354bcf727b57c57b785fa03c6f1258982a3ec01109e543051fa9f8189ff006e69225fc4543bb6569d3d2aae2535c5671059f09542d89beb453aaf81c5f649121932c322abec45702e209aaa7e26b7c43fd547c8b4b2abec3f74cfe52ad79bd979af6a78c784cb754fc80ab0c55c377938a6bf851c54ff8994f27482b17654ee0c323a77469da94b72017b754fe5703e2bdcf292636b8c5e7286fa7e6242cf633c3ee9c4c3ad36e9f3e2eb0216fcc63dc64bb5f25ae4a542f7c3ccf6d639f5f9f777fb74d9d0a6cdda42c02d5e115bacb62ef0c38897979a3e1a5df0277d3f3f3a35b9df31547ce635298baecce9116bfb57eb989ee6cfe2cdf7cee94ce9b4c31d8ee3cab7719dea74f1a8c5015ceaf8e5bbd2e8d82097dda4d6949b87e594309180bc9adc8599e4f3a7d9471cdeed1cf3282cf743f721bd802a2022d9964d2049a576eaecb0b5f6e8cebe69833ee565594dfb3766ac4cee4b3221c8de6e996d8c25f5bdb2010e61bb2ebf0733b671e44e0e39c0d8ae3fdb4ec85d7f5296eb80ed13007cfd07578ff80ef37d7fb018ef2e79b1c7d50b1833335ed8f07b1939f02bbb09b31184b4450c01770be7106fe2b507cd7e0f39616dc80d2946d08d07003ab7ae6101c6a686c6a9e41e175a82dbe86dfe16b9cc56a0ffec29a16bf08f9af429d43111115b7f843fe906f16251e0cba7e21ff2c4abd189c43d96290b537501ef2fd4a083e17fa7614ba504bf8aa4129452923e87274a2028f611d8e228493d880096cc439fe30dce10ae252c8d093b387d0e2523e8f56ce3c8c328436ec21e99d88d2ff619ed6c9957d68871ffb3312a52d1db41ca0652dfc85fb44d13e710b3b15742a38a8e0111ce24a017da3fc7c946f5217048685b10bdd0c2ef334c283651eaa72b4ada09439b249eedeacb46d71994b5e15e9ed0bbcaa32bc243a3f3c4497a9909e05588733b014b100a81747e82293bd8bc0a45217e5f9b35847b0995c7597aeef21a090408b4fe66c83c065ec95b38d82182b5bfc4d327b329573d8c41d9b99bdaad26a0e21fffcac740b8719d4f45cbb7db3d94b87adbed80c6a7bb277dc9371695ecc78037983a51f64e997f2a91c8db437315fcd1826c1115e0093e57f811740aab283dce57a1fb5f04b36197d82fc2fd1cffa60a7878563ccac87b11218a09fd7cdb1d433ed35b8e0f5386d52cf8df0dce63f0ebf822105c7996905fc0e7c12f887cbd9ea7a70c21d4f122a18c4c302ad43bd1bba8ed03dff02504b0708d4b274262a0600004e0d0000504b010214001400080808005455924e6c47f91fe203000036080000250004000000000000000000000000000000526576696577436f6e74726163742457726974655265766965774576656e742e636c617373feca0000504b010214001400080808005455924eace91217c3030000f00700001b0000000000000000000000000039040000526576696577436f6e7472616374245265766965772e636c617373504b010214001400080808005455924ed4b274262a0600004e0d0000140000000000000000000000000045080000526576696577436f6e74726163742e636c617373504b05060000000003000300e2000000b10e00000000'
        # methodk = "imputedContractCreateGas"
        # p_list = [self.chainId, self.senderk, hex, []]
        # request = self.setup_top(methodk, p_list)
        # resp1 = self.send_request(request)
        # gasLimit = resp1["gasLimit"]  ## don't know why it says this-- ?
        # print("gaslimit: ", gasLimit)
        # gasLimit = gasLimit * 10**3  # gas must be less than 10000000","data":null
        # # gasLimit = gasLimit
        g_limit = 9000000
        return g_limit


if __name__ == "__main__":
    c = GetGasLimit()
    g = c.get_gas_limit()
    print(g)



  #
  # Map<String, Object> parameters = new HashMap<>();
  #       parameters.put("sender", sender);
  #       parameters.put("gasLimit", form.getGasLimit());
  #       parameters.put("price", form.getPrice());
  #       parameters.put("password", password);
  #       parameters.put("remark", form.getRemark());
  #       parameters.put("contractAddress", form.getContractAddress());
  #       parameters.put("value", form.getValue());
  #       parameters.put("methodName", form.getMethodName());
  #       parameters.put("methodDesc", form.getMethodDesc());
  #       parameters.put("args", contractArgs);
  #       RpcClientResult result = restFul.post("/contract/call", parameters);
  #       if (result.isFailed()) {
  #           return CommandResult.getFailed(result);
  #


#
'''
{
  "contractAddress": "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
  "createTxHash": "7a2aa78e85cdf37a72e88da25c82acfdff57a5a786718909e2c4d50cc3c45cf5",
  "creater": "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7",
  "gasLimit": 11725,
  "price": 25,
  "methodName": "writeReview",
  "methodDesc": "(String productId, String reviewComments) return LReviewContract$Review;",
  "args": "[[\"baseballOutfit\"],[\"fit a little large\"]]",
  "value": 0,
  "resultInfo": {
    "txHash": "7a2aa78e85cdf37a72e88da25c82acfdff57a5a786718909e2c4d50cc3c45cf5",
    "contractAddress": "TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM",
    "success": true,
    "errorMessage": null,
    "result": "{\"productId\":\"baseballOutfit\",\"comments\":\"fit a little large\",\"writer\":\"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7\"}",
    "gasLimit": 11725,
    "gasUsed": 7817,
    "price": 25,
    "totalFee": "0.00393125",
    "txSizeFee": "0.001",
    "actualContractFee": "0.00195425",
    "refundFee": "0.000977",
    "value": "0",
    "nulsTransfers": [],
    "tokenTransfers": [],
    "remark": "call",
    "contractTxList": [],
    "events": [
      "{\"contractAddress\":\"TTSETeCA3FueL9cKCiDR8vAiRiGVtVCJksEsstM\",\"blockNumber\":390697,\"event\":\"WriteReviewEvent\",\"payload\":{\"productId\":\"baseballOutfit\",\"reviewComments\":\"fit a little large\",\"writer\":\"TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7\"}}"
    ]
  }
}
'''

'''
@Parameters(value = {
        @Parameter(parameterName = "chainId", requestType = @TypeDescriptor(value = int.class), parameterDes = "链id"),
        @Parameter(parameterName = "sender",  parameterDes = "交易创建者账户地址"),
        @Parameter(parameterName = "password",  parameterDes = "调用者账户密码"),
        @Parameter(parameterName = "value", requestType = @TypeDescriptor(value = BigInteger.class), parameterDes = "调用者向合约地址转入的主网资产金额，没有此业务时填BigInteger.ZERO"),
        @Parameter(parameterName = "gasLimit", requestType = @TypeDescriptor(value = long.class), parameterDes = "GAS限制"),
        @Parameter(parameterName = "price", requestType = @TypeDescriptor(value = long.class), parameterDes = "GAS单价"),
        @Parameter(parameterName = "contractAddress",  parameterDes = "合约地址"),
        @Parameter(parameterName = "methodName",  parameterDes = "合约方法"),
        @Parameter(parameterName = "methodDesc",  parameterDes = "合约方法描述，若合约内方法没有重载，则此参数可以为空", canNull = true),
        @Parameter(parameterName = "args", requestType = @TypeDescriptor(value = Object[].class), parameterDes = "参数列表", canNull = true),
        @Parameter(parameterName = "remark",  parameterDes = "交易备注", canNull = true)

'''


