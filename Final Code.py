from experta import *

class SoftwareProjectsConsultant (KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="Q1")
        
    @Rule(Fact(action='Q1'), NOT(Fact(Q_Applicatio=W())))
    def IsItApplicatio(self):
        self.declare(Fact(Q_Applicatio=input("Do you want to make an Application ? ")))
    
        #Application
    
    @Rule(Fact(Q_Applicatio='y'), NOT(Fact(Android=W())))
    def IsItAndroid(self):
        self.declare(Fact(Android=input("Is it Android ? ")))
        
    @Rule(Fact(Android='y'), NOT(Fact(Android1=W())))
    def NeedWeb(self):
        self.declare(Fact(Android1=input("Do you want your app to have accessed via a web browser on your mobile device ? ")))
    

    @Rule(Fact(Android1='y'), NOT(Fact(A1=W())))
    def A_1(self):
        self.declare(Fact(A1=input("Do you have any experience using Python ? ")))
    
    @Rule(Fact(A1='n'), NOT(Fact(A11=W())))
    def A_11(self):
        self.declare(Fact(A11=input("Do you have any experience using PHP ? ")))
    
    @Rule(Fact(A11='y'), NOT(Fact(A111=W())))
    def A_111(self):
        self.declare(Fact(A111=input("Do you have any experience using JavaScript ? ")))
    
    @Rule(Fact(A111='y'), NOT(Fact(A1111=W())))
    def A_1111(self):
        self.declare(Fact(A1111=input("Do you need AI ? ")))
    
    @Rule(Fact(A1111='y'))
    def A_1111WAI(self):
        print(
            "\nYou can use Vue-JS for FrontEnd and Laravel for BackEnd then for the AI you can use Phpml and rubix librarys"
             )
    
    @Rule(Fact(A1111='n'))
    def A_1111NOAI(self):
        print("\nYou can use Vue-JS for FrontEnd and Laravel for BackEnd ")
    
    @Rule(Fact(A111='n'), NOT(Fact(A1112=W())))
    def A_1112(self):
        self.declare(Fact(A1112=input("Do you need AI ? ")))
        
    @Rule(Fact(A1112='y'))
    def A_1112WAI(self):
        print(
              "\nYou can use Boostrap for FrontEnd and Laravel for BackEnd"
              "\n then for the AI you can use Phpml and rubix librarys"
              )
    
    @Rule(Fact(A1112='n'))
    def A_1112NOAI(self):
        print("\nYou can use Boostrap for FrontEnd and Laravel for BackEnd ")
    
    @Rule(Fact(A11='n'), NOT(Fact(A112=W())))
    def A_112(self):
        self.declare(Fact(A112=input("Do you have any experience using JavaScript ? ")))
    
    @Rule(Fact(A112='y'), NOT(Fact(A1121=W())))
    def A_1121(self):
        self.declare(Fact(A1121=input("Do you need AI ? ")))
        
    @Rule(Fact(A1121='y'))
    def A_1121WAI(self):
        print(
              "\nYou can use Veu-JS for FrontEnd and for the BackEnd Ruby on Rails with the librarys openNLP, tts and ruby_fan for the AI"
              "\n or you can use Kotlin with the librarys SimpleDDN, Kotlin_Statisticswith, Apacha Jena, Tweety, Neuroph and weka for the AI"
               )
    
    @Rule(Fact(A1121='n'))
    def A_1121NOAI(self):
        print("\nYou can use Veu-JS for FrontEnd and Ruby on Rails OR Kotlin for BackEnd ")
    
    @Rule(Fact(A112='n'), NOT(Fact(A1122=W())))
    def A_1122(self):
        self.declare(Fact(A1122=input("Do you need AI ? ")))
         
    @Rule(Fact(A1122='y'))
    def A_1122WAI(self):
        print(
              "\nYou can use Boostrap for FrontEnd and for the BackEnd you can"
              "\nuse Ruby on Rails with the librarys openNLP, tts and ruby_fan for the AI"
              "\nor you can use Kotlin with the librarys SimpleDDN, Kotlin_Statisticswith,"
              "\nApacha Jena, Tweety, Neuroph and weka for the AI"
             )
    
    @Rule(Fact(A1122='n'))
    def A_1122NOAI(self):
        print("You can use Boostrap for FrontEnd and Ruby on Rails or Kotlin for BackEnd ")
    
    @Rule(Fact(A1='y'), NOT(Fact(A12=W())))
    def A_12(self):
        self.declare(Fact(A12=input("Do you have any experience using JavaScript ? ")))
    
    @Rule(Fact(A12='y'), NOT(Fact(A121=W())))
    def A_121(self):
        self.declare(Fact(A121=input("Do you need AI ? ")))
    
    @Rule(Fact(A121='y'))
    def A_121WAI(self):
        print(
              "\nYou can use Veu-JS for FrontEnd and Django for BackEnd with"
              "\nCaffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI"
               )
    
    @Rule(Fact(A121='n'))
    def A_121NOAI(self):
        print("You can use Veu-JS for FrontEnd and Django for BackEnd ")
        
    @Rule(Fact(A12='n'), NOT(Fact(A122=W())))
    def A_122(self):
        self.declare(Fact(A122=input("Do you need AI ? ")))
        
    @Rule(Fact(A122='y'))
    def A_122WAI(self):
        print(
              "\nYou can use Boostrap for FrontEnd and Django for BackEnd with"
              "\nCaffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI"
              )
    
    @Rule(Fact(A122='n'))
    def A_122NOAI(self):
        print("\nYou can use Boostrap for FrontEnd and Django for BackEnd ")
    
    @Rule(Fact(Android1='n'), NOT(Fact(A2=W())))
    def A_2(self):
        self.declare(Fact(A2=input("Do you have any experience using Python ? ")))
        
    @Rule(Fact(A2='y'), NOT(Fact(A21=W())))
    def A_21(self):
        self.declare(Fact(A21=input("Do you have any experience using JavaScript ? "))) 
    
    @Rule(Fact(A21='y'), NOT(Fact(A211=W())))
    def A_211(self):
        self.declare(Fact(A211=input("Do you need AI ? ")))
        
    @Rule(Fact(A211='y'))
    def A_211WAI(self):
        print(
              "\nYou can use React for FrontEnd and Django for BackEnd with"
              "\nCaffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI"
              )
    
    @Rule(Fact(A211='n'))
    def A_211NOAI(self):
        print("\nYou can use React for FrontEnd and Django or Flask for BackEnd ")
    
    @Rule(Fact(A21='n'), NOT(Fact(A212=W())))
    def A_212(self):
        self.declare(Fact(A212=input("Do you need AI ? ")))
        
    @Rule(Fact(A212='y'))
    def A_212WAI(self):
        print(
              "\nYou can use Flutter for FrontEnd and Django for BackEnd with"
              "\nCaffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI"
              )
    
    @Rule(Fact(A212='n'))
    def A_212NOAI(self):
        print("\nYou can use Flutter for FrontEnd and Django or Flask for BackEnd ")
     
    @Rule(Fact(A2='n'), NOT(Fact(A22=W())))
    def A_22(self):
        self.declare(Fact(A22=input("Do you have any experience using PHP ? ")))
        
    @Rule(Fact(A22='y'), NOT(Fact(A221=W())))
    def A_221(self):
        self.declare(Fact(A221=input("Do you have any experience using JavaScript ? "))) 
    
    @Rule(Fact(A221='y'), NOT(Fact(A2211=W())))
    def A_2211(self):
        self.declare(Fact(A2211=input("Do you need AI ? ")))
        
    @Rule(Fact(A2211='y'))
    def A_2211WAI(self):
        print("\nYou can use React for FrontEnd and Laravel or Codeigniter for BackEnd with Phpml and rubix librarys for the AI")
    
    @Rule(Fact(A2211='n'))
    def A_2211NOAI(self):
        print("\nYou can use React for FrontEnd and Laravel or Codeigniter for BackEnd  ")
    
    @Rule(Fact(A221='n'), NOT(Fact(A2212=W())))
    def A_2212(self):
        self.declare(Fact(A2212=input("Do you need AI ? ")))
        
    @Rule(Fact(A2212='y'))
    def A_2212WAI(self):
        print(
              "\nYou can use Flutter for FrontEnd and Laravel or Codeigniter for the BackEnd"
              "\nwith Phpml and rubix librarys for the AI"
              )
    
    @Rule(Fact(A2212='n'))
    def A_2212NOAI(self):
        print("\nYou can use Flutter for FrontEnd and Laravel or Codeigniter for BackEnd")
    
    @Rule(Fact(A22='n'), NOT(Fact(A222=W())))
    def A_222(self):
        self.declare(Fact(A222=input("Do you have any experience using JavaScript ? "))) 
    
    @Rule(Fact(A222='y'), NOT(Fact(A2221=W())))
    def A_2221(self):
        self.declare(Fact(A2221=input("Do you need AI ? ")))
        
    @Rule(Fact(A2221='y'))
    def A_2221WAI(self):
        print(
              "\nYou can use React for FrontEnd and and for the BackEnd Ruby on Rails with the librarys openNLP, tts and ruby_fan for the AI"
              "\n or you can use Kotlin with the librarys SimpleDDN, Kotlin_Statisticswith, Apacha Jena, Tweety, Neuroph and weka for the AI"
              )
    
    @Rule(Fact(A2221='n'))
    def A_2221NOAI(self):
        print("\nYou can use React for FrontEnd and Ruby on Rails or Kotlin for BackEnd ")
    
    @Rule(Fact(A222='n'), NOT(Fact(A2222=W())))
    def A_2222(self):
        self.declare(Fact(A2222=input("Do you need AI ? ")))
        
    @Rule(Fact(A2222='y'))
    def A_2222WAI(self):
        print(
              "\nYou can use Flutter for FrontEnd and and for the BackEnd Ruby on Rails with the librarys openNLP and tts and ruby_fan for the AI"
              "\n or you can use Kotlin with the librarys SimpleDDN, Kotlin_Statisticswith, Apacha Jena, Tweety, Neuroph and weka for the AI"
              )
    
    @Rule(Fact(A2222='n'))
    def A_2222NOAI(self):
        print("\nYou can use Flutter for FrontEnd and Ruby on Rails or Kotlin for BackEnd")
    
    
            #Web part
    
    
    @Rule(Fact(Q_Applicatio='n'), NOT(Fact(Web=W())))
    def ItItWeb(self):
        self.declare(Fact(Web=input("Do you want to make it a Website ? ")))
    
    @Rule(Fact(Web='y'), NOT(Fact(exp=W())))
    def Expert(self):
        self.declare(Fact(exp=input("Do you have any experince in web development ? ")))
    
    @Rule(Fact(exp='n'), NOT(Fact(W1=W())))
    def W_1(self):
        self.declare(Fact(W1=input("Is it an active website (like buying things from it) ? ")))
    
    @Rule(Fact(W1='y'), NOT(Fact(W11=W())))
    def W_11(self):
        self.declare(Fact(W11=input("Would you need AI ? ")))
    
    @Rule(Fact(W11='y'))
    def W_11WAI(self):
        print(
              "\nYou can use Ember for the FrontEnd and for the BackEnd you can use Ruby on Rails with openNLP, tts and ruby_fan for the librarys AI"
              "\nor Django useing Caffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI"
              )
    
    @Rule(Fact(W11='n'))
    def W_11NOAI(self):
        print("\nYou can use Ember for the FrontEnd and Ruby on Rails or Django for BackEnd ")
        
    @Rule(Fact(W1='n'), NOT(Fact(W12=W())))
    def W_12(self):
        self.declare(Fact(W12=input("Would you need AI ? ")))
    
    @Rule(Fact(W12='y'))
    def W_12WAI(self):
        print("\nYou can use only Django for both Front and Back End useing Caffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI")
    
    @Rule(Fact(W12='n'))
    def W_12NOAI(self):
        print("\nYou can use only Django for both Front and Back End  ")
    
    @Rule(Fact(exp='y'), NOT(Fact(W2=W())))
    def W_2(self):
        self.declare(Fact(W2=input("Is it an active website (like buying things from it) ? ")))
        
    @Rule(Fact(W2='y'), NOT(Fact(W21=W())))
    def W_21(self):
        self.declare(Fact(W21=input("Do you have any experience using PHP ? ")))
    
    @Rule(Fact(W21='y'), NOT(Fact(W211=W())))
    def W_211(self):
        self.declare(Fact(W12=input("Would you need AI ? ")))
    
    @Rule(Fact(W211='y'))
    def W_211WAI(self):
        print(
              "\nYou can use Vue-JS for FrontEnd and laravel for BackEnd with Phpml and rubix librarys for the AI"
              "\nor Codeigniter with Phpml and rubix librarys fot the AI"
              )
    
    @Rule(Fact(W211='n'))
    def W_211NOAI(self):
        print("\nYou can use Vue-JS for FrontEnd and Laravel or Codeigniter for the BackEnd ")
    
    @Rule(Fact(W21='n'), NOT(Fact(W212=W())))
    def W_212(self):
        self.declare(Fact(W212=input("Would you need AI ? ")))
    
    @Rule(Fact(W212='y'))
    def W_212WAI(self):
        print(
              "\nYou can use Ember for the FrontEnd and for the BackEnd Ruby on Rails"
              "\nwith the librarys openNLP, tts and ruby_fan for the AI"
              "\nor Kotlin with SimpleDDN and Kotlin_Statistics librarys for the AI"
              )
    
    @Rule(Fact(W211='n'))
    def W_212NOAI(self):
        print("\nYou can use Ember for the FrontEnd and Ruby on Rails or Kotlin for BackEnd ")
    
    @Rule(Fact(W2='n'), NOT(Fact(W22=W())))
    def W_22(self):
        self.declare(Fact(W22=input("Do you have any experience using JavaScript ? ")))
    
    @Rule(Fact(W22='y'), NOT(Fact(W221=W())))
    def W_221(self):
        self.declare(Fact(W221=input("Would you need AI ? ")))
    
    @Rule(Fact(W221='y'))
    def W_221WAI(self):
        print(
              "\nYou can use React-JS or Vue-JS or Angularfor the FrontEnd and Node-JS for the BackEnd with"
              "\nthen TensorFlow.js, TorchJS, ml.js and brain.js librarys for AI "
              )
    
    @Rule(Fact(W221='n'))
    def W_221NOAI(self):
        print("\nYou can use React-JS or Vue-JS or Angular for the FrontEnd and Node-JS for the BackEnd ")
    
    @Rule(Fact(W22='n'), NOT(Fact(W222=W())))
    def W_222(self):
        self.declare(Fact(W222=input("Do you have any experience using Python ?")))
    
    @Rule(Fact(W222='y'), NOT(Fact(W2221=W())))
    def W_2221(self):
        self.declare(Fact(W2221=input("Would you need AI ? ")))
    
    @Rule(Fact(W2221='y'))
    def W_2221WAI(self):
        print(
              "\nYou can use Boostrap for the FrontEnd and Django for the BackEnd with"
              "\nCaffe, Caffe2, OpenCV, Keras and NeuroLab librarys for the AI"
              )
    
    @Rule(Fact(W2221='n'))
    def W_2221NOAI(self):
        print("\nYou can use Boostrap for the FrontEnd and Flask or Django for the BackEnd or even you can use only Django for both Front and Back")
    
    @Rule(Fact(W222='n'), NOT(Fact(W2222=W())))
    def W_2222(self):
        self.declare(Fact(W2222=input("Would you need AI ? ")))
    
    @Rule(Fact(W2222='y'))
    def W_2222WAI(self):
        print(
              "\nYou can use Ember for the FrontEnd for the BackEnd you can use Ruby on Rails with openNLP, tts and ruby_fan librarys for the AI"
              "\nor you can use Kotlin with SimpleDDN and Kotlin_Statistics librarys for the AI"
              )
    
    @Rule(Fact(W2222='n'))
    def W_2222NOAI(self):
        print("\nYou can use Ember for the FrontEnd and Ruby on Rails or Kotlin for BackEnd ")
        
        #Windows part
    
    @Rule(Fact(Android='n'), NOT(Fact(Windows=W())))
    def NeedWindows(self):
        self.declare(Fact(Windows=input("Is it Windows ? ")))
    
    @Rule(Fact(Windows='y'), NOT(Fact(I1=W())))
    def I_1(self):
        self.declare(Fact(I1=input("Do you need internet accsse while using the app ? ")))
    
    @Rule(Fact(I1='n'), NOT(Fact(I11=W())))
    def I_11(self):
        self.declare(Fact(I11=input("Do you have any experience using C# ? ")))
        
    @Rule(Fact(I11='n'), NOT(Fact(I112=W())))
    def I_112(self):
        self.declare(Fact(I112=input("Do you need AI ? ")))
    
    @Rule(Fact(I112='y'))
    def I_112WAI(self):
        print(
              "\nYou can use Flutter with Visual Studio Code using Dart and you can use starflut package to include Python with"
              "\nthe librarys Caffe, Caffe2, OpenCV, Keras and NeuroLab for the AI"
              "\nor java with the librarys Apacha Jena, Tweety, Neuroph and weka for the AI"
              )
    
    @Rule(Fact(I112='n'))
    def I_112NOAI(self):
        print("\nYou can use Flutter with Visual Studio Code using Dart and you can use starflut package to include python, java, ruby, golang, rust, etc. ")
    
    @Rule(Fact(I11='y'), NOT(Fact(I111=W())))
    def I_111(self):
        self.declare(Fact(I111=input("Do you have any experience using Windows Forms ? ")))
    
    @Rule(Fact(I111='y'), NOT(Fact(I1111=W())))
    def I_1111(self):
        self.declare(Fact(I1111=input("Do you need AI ? ")))
    
    @Rule(Fact(I1111='y'))
    def I_1111WAI(self):
        print("\nYou can use Windows Forms with Visual Studio using C# and the single form can support up to 11 languages and you can download a pre-trained mode")
    
    @Rule(Fact(I1111='n'))
    def I_1111NOAI(self):
        print("\nYou can use Windows Forms with Visual Studio using C# and the single form can support up to 11 languages ")
    
    @Rule(Fact(I111='n'), NOT(Fact(I1112=W())))
    def I_1112(self):
        self.declare(Fact(I1112=input("Do you have any experience using WPF ? ")))
    
    @Rule(Fact(I1112='y'), NOT(Fact(I11121=W())))
    def I_11121(self):
        self.declare(Fact(I11121=input("Do you need AI ? ")))
    
    @Rule(Fact(I11121='y'))
    def I_11121WAI(self):
        print("\nYou can use Windows Forms with Visual Studio using C# and the single form can support up to 11 languages and you can download a pre-trained mode")
    
    @Rule(Fact(I112='n'))
    def I_11121NOAI(self):
        print("\nYou can use WPF with Visual Studio using C#and can support C# and XML")
    
    @Rule(Fact(I1112='n'), NOT(Fact(I11122=W())))
    def I_11122(self):
        self.declare(Fact(I11122=input("Do you have any experience using UWP?")))
    
    @Rule(Fact(I11122='y'), NOT(Fact(I111221=W())))
    def I_111221(self):
        self.declare(Fact(I11121=input("Do you need AI ? ")))
    
    @Rule(Fact(I111221='y'))
    def I_111221WAI(self):
        print("\nYou can use wpf with Visual Studio using C# and the single form can support up to 11 languages and you can download a pre-trained mode")
    
    @Rule(Fact(I111221='n'))
    def I_111221NOAI(self):
        print("\nYou can use WPF with Visual Studio using C# and can support C++,  C# and JavaScript ")
    
    @Rule(Fact(I1='y'), NOT(Fact(I12=W())))
    def I_12(self):
        self.declare(Fact(I12=input("Do you have any experience using Flutter ? ")))

    @Rule(Fact(I12='y'), NOT(Fact(I121=W())))
    def I_111221(self):
        self.declare(Fact(I121=input("Do you need AI ? ")))
    
    @Rule(Fact(I121='y'))
    def I_121WAI(self):
        print(
               "\nYou can use Windows Forms with Visual Studio using C# and the single form can support up to 11 languages and"
              "\nyou can download a pre-trained mode then placing a Visual WAO DLL in these projects on the client side and on the application server side"
              )
    
    @Rule(Fact(I121='n'))
    def I_121NOAI(self):
        print(
              "\nYou can use Windows Forms with Visual Studio using C# and the single form can support up to 11 languages then"
              "\nplacing a Visual WAO DLL in these projects on the client side and on the application server side "
            )
       
    @Rule(Fact(I12='n'), NOT(Fact(I122=W())))
    def I_122(self):
        self.declare(Fact(I122=input("Do you need AI ? ")))
    
    @Rule(Fact(I122='y'))
    def I_122WAI(self):
        print(
              "\nYou can use Flutter with Visual Studio Code using Dart and Django for BacEend with"
              "\nCaffe and Caffe2 and OpenCV and Keras and NeuroLab librarys for the AI"
              )
    
    @Rule(Fact(I122='n'))
    def I_122NOAI(self):
        print("\nYou can use Flutter with Visual Studio Code using Dart for the FrontEnd and you can use Flask or Django for Backend ")
        
        
        #Games

    @Rule(Fact(Web='n'), NOT(Fact(Q_game=W())))
    def IsItGame(self):
        self.declare(Fact(Q_game=input("Do you want to make a video game ? ")))
    
    #Q_game
    @Rule(Fact(Q_game='y'), NOT(Fact(experienceg=W())))
    def experience(self):
        self.declare(Fact(experienceg=input("Do you any experience with making video games ? ")))
        
    
    #experienceg
    @Rule(Fact(experienceg='n'))
    def Scratch(self):
         print(
              "\nYou can use Scratch,it uses a high-level block-based visual programing language,"
              "\nthat makes video games development understandable and so easy"
              )

    @Rule(Fact(experienceg='y'), NOT(Fact(moderateH=W())))
    def moderateH1(self):
        self.declare(Fact(moderateH=input("Do you have a moderate hardware ? ")))
    
    #moderateH 
    @Rule(Fact(moderateH='n'))
    def Blender(self):
         print(
              "\nYou can use Blender 2.79 or less, it can make 3D objects and have ease-to-use logic panel"
              "\nthat uses logic gates to make the game interactive with the player"
              )

############################################--Unity--#########################################################
    #Have you deal with Unity?
    @Rule(Fact(moderateH='y'), NOT(Fact(Unity=W())))
    def Q_Unity(self):
        self.declare(Fact(Unity=input("Have you deal with Unity ? ")))


    #Do you have any experience making 3D objects
    @Rule(Fact(Unity='y'), NOT(Fact(Unityqy=W())))
    def Unity_y(self):
        self.declare(Fact(Unityqy=input("Do you have any experience making 3D objects ? ")))  

    #Do you any programming experience?
    @Rule(Fact(Unityqy='y'), NOT(Fact(Unityqyy=W())))
    def Unity_yy(self):
        self.declare(Fact(Unityqyy=input("Do you any programming experience ? ")))

    #Is it for mobile?
    @Rule(Fact(Unityqyy='y'), NOT(Fact(Unityqyyy=W())))
    def Unity_yyy(self):
        self.declare(Fact(Unityqyyy=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unityqyyy='y'))
    def Unity_yyyy(self):
        print(
              "\nYou can use Unity engine using C# to build your game then"
              "\nfor 3D objects you can make them using any 3d computer graphics"
              "\nyou should make Low-poly to make the graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unityqyyy='n'))
    def Unity_yyyn(self):
        print(
              "\nYou can use Unity engine using C# to build your game"
              "\nthen for 3D objects you can make them using any 3d computer graphics"
              )

    #Is it for mobile?
    @Rule(Fact(Unityqyy='n'), NOT(Fact(Unityqyyn=W())))
    def Unity_yyn(self):
        self.declare(Fact(Unityqyyn=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unityqyyn='y'))
    def Unity_yyny(self):
        print(
              "\nYou can use Unity engine using Visual Scripting! (Unity, Bolt) to build your game"
              "\nthen for 3D objects you can make them using any 3d computer graphics"
              "\nyou should make Low-poly to make the graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unityqyyn='n'))
    def Unity_yynn(self):
        print(
              "\nYou can use Unity engine using Visual Scripting! (Unity, Bolt)to build your game"
              "\nthen for 3D objects you make them using any 3d computer graphics"
              )

#############################################################################

    #Do you any programming experience?
    @Rule(Fact(Unityqy='n'), NOT(Fact(Unityqyn=W())))
    def Unity_yn(self):
        self.declare(Fact(Unityqyn=input("Do you any programming experience ? ")))

    #Is it for mobile?
    @Rule(Fact(Unityqyn='y'), NOT(Fact(Unityqyny=W())))
    def Unity_yny(self):
        self.declare(Fact(Unityqyny=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unityqyny='y'))
    def Unity_ynyy(self):
        print(
              "\nYou can use Unity engine using C# to build your game"
              "\nthen for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com you should download Low-poly"
              "\nto make the graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unityqyny='n'))
    def Unity_ynyn(self):
        print(
              "\nYou can use Unity engine using C# to build your game"
              "\nthen for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com"
              )

    #Is it for mobile?
    @Rule(Fact(Unityqyn='n'), NOT(Fact(Unityqynn=W())))
    def Unity_ynn(self):
        self.declare(Fact(Unityqynn=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unityqynn='y'))
    def Unity_ynny(self):
        print(
              "\nYou can use Unity engine using Visual Scripting! (Unity, Bolt)"
              "\nto build your game then for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com you should download Low-poly"
              "\nto make the graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unityqynn='n'))
    def Unity_ynnn(self):
        print(
              "\nYou can use Unity engine using Visual Scripting! (Unity, Bolt)"
              "\nto build your game then for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com"
              )


###############################--Unreal--##############################################


    #Have you deal with Unreal?
    @Rule(Fact(Unity='n'), NOT(Fact(Unreal=W())))
    def Q_Unreal(self):
        self.declare(Fact(Unreal=input("Have you deal with Unreal ? ")))


    #Do you have any experience making 3D objects
    @Rule(Fact(Unreal='y'), NOT(Fact(Unrealqy=W())))
    def Unreal_y(self):
        self.declare(Fact(Unrealqy=input("Do you have any experience making 3D objects ? ")))  

    #Do you any programming experience?
    @Rule(Fact(Unrealqy='y'), NOT(Fact(Unrealqyy=W())))
    def Unreal_yy(self):
        self.declare(Fact(Unrealqyy=input("Do you any programming experience ? ")))

    #Is it for mobile?
    @Rule(Fact(Unrealqyy='y'), NOT(Fact(Unrealqyyy=W())))
    def Unreal_yyy(self):
        self.declare(Fact(Unrealqyyy=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unrealqyyy='y'))
    def Unreal_yyyy(self):
        print(
              "\nYou can use Unreal engine using C++ to build your game"
              "\nthen for 3D objects you can make them using any 3d computer graphics"
              "\nyou should make Low-poly to make the graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unrealqyyy='n'))
    def Unreal_yyyn(self):
        print(
              "\nYou can use Unreal engine using C++ to build your game then"
              "\nfor 3D objects you can make them using any 3d computer graphics"
              )

    #Is it for mobile?
    @Rule(Fact(Unrealqyy='n'), NOT(Fact(Unrealqyyn=W())))
    def Unreal_yyn(self):
        self.declare(Fact(Unrealqyyn=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unrealqyyn='y'))
    def Unreal_yyny(self):
        print(
              "\nYou can use Unreal engine using Blueprint Visual Scripting system"
              "\nto build your game then for 3D objects you can make them using"
              "\nany 3d computer graphics you should make Low-poly to make"
              "\nthe graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unrealqyyn='n'))
    def Unreal_yynn(self):
        print(
              "\nYou can use Unreal engine using Blueprint Visual Scripting system to build"
              "\nyour game then for 3D objects you make them using any 3d computer graphics"
              )

#############################################################################

    #Do you any programming experience?
    @Rule(Fact(Unrealqy='n'), NOT(Fact(Unrealqyn=W())))
    def Unreal_yn(self):
        self.declare(Fact(Unrealqyn=input("Do you any programming experience ? ")))

    #Is it for mobile?
    @Rule(Fact(Unrealqyn='y'), NOT(Fact(Unrealqyny=W())))
    def Unreal_yny(self):
        self.declare(Fact(Unrealqyny=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unrealqyny='y'))
    def Unreal_ynyy(self):
        print(
              "\nYou can use Unreal engine using C++ to build your game then"
              "\nfor 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com you should download Low-poly"
              "\nto make the graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unrealqyny='n'))
    def Unreal_ynyn(self):
        print(
              "\nYou can use Unreal engine using C++ to build your game"
              "\nthen for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com"
              )

    #Is it for mobile?
    @Rule(Fact(Unrealqyn='n'), NOT(Fact(Unrealqynn=W())))
    def Unreal_ynn(self):
        self.declare(Fact(Unrealqynn=input("Is it for mobile ? ")))

    #DDDDDD
    @Rule(Fact(Unrealqynn='y'))
    def Unreal_ynny(self):
        print(
              "\nYou can use Unreal engine using Blueprint Visual Scripting system to build your game"
              "\nthen for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com you should download Low-poly to make"
              "\nthe graphics flexible for rendering on the mobile"
              )
    #DDDDDD
    @Rule(Fact(Unrealqynn='n'))
    def Unreal_ynnn(self):
        print(
              "\nYou can use Unreal engine using Blueprint Visual Scripting system to build your game"
              "\nthen for 3D objects you can download them from any website like:"
              "\nwww.cgtrader.com www.free3d.com"
              )



        
engine = SoftwareProjectsConsultant()
engine.reset() # Prepare the engine for the execution.
engine.run() # Run it!
