
import unittest

from Assignments.Ex3.src.DiGraph import DiGraph
from Assignments.Ex3.src.MyNodeData import MyNodeData
#POKIMONIMONIM HAYOU LEFI IRUIM

class test_DiGraph(unittest.TestCase):#izrok hariga ba mida ve
    #samti le mikbalot
    def creat_g(self)-> DiGraph: #mishtamesh be le kol funkziot bdika aharkah
        g = DiGraph()
        for i in range(10):
            g.add_node(i)

        for i in range(10):
            if(i ==5):
                continue
            g.add_edge(5,i,10.5)


        return g #zurat kohav 5 mehubar le harbe zurat kohav


    def test_get_v(self): #need to do public function

        g=self.creat_g()
        self.assertTrue(g.get_v(1).getkey(),1) #bodkim ki maf
        self.assertNotEqual(g.get_v(1).getkey(), 2)  # bodkim ki maf


    def test_v_size(self):
        g=self.creat_g()
        x = g.v_size()
        self.assertEqual(x,10)




    def test_get_all_v(self):
        g = self.creat_g()
        r = list(g.get_all_v().keys())
        p = [0,2]
       # for k, v in g.get_all_v().items():
        self.assertEqual(r[0],p[0])



    def test_all_in_edges_of_node(self):
        # zlaot yozot
        g = self.creat_g()
        edges_of_node = list(g.all_in_edges_of_node(5).keys())
        # print(edges_of_node)
        a = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        j = 0
        for i in range(len(edges_of_node)):
            # print(edges_of_node[i],a[i])
            self.assertEqual(edges_of_node[i], a[i])




    def test_all_out_edges_of_node(self):
        #zlaot yozot
        g = self.creat_g()
        edges_of_node = list(g.all_in_edges_of_node(5).keys())
        #print(edges_of_node)
        a = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        j = 0
        for i in range(len(edges_of_node)):
           # print(edges_of_node[i],a[i])
            self.assertEqual(edges_of_node[i], a[i])



    def test_e_size(self): #lispor kamut zlaot
        g = self.creat_g()
        l = g.e_size()
        len_is = 9
        self.assertTrue(l,len_is)





    def test_get_mc(self):
        total_change = 19
        g = self.creat_g()
        l = g.get_mc()
        self.assertTrue(total_change,l)

    def test_add_edge(self):

        g = self.creat_g()
        g.add_edge(2,3,10)
        self.assertTrue(g.e_size(),10)




    def test_add_node(self):

        g = self.creat_g()
        g.add_node(11)
        self.assertEqual(g.v_size(),11)


    def test_remove_node(self):
        g = self.creat_g()
        g.remove_node(0)

        self.assertTrue(g.v_size(),9)

        g.remove_node(5)

        self.assertEqual(g.v_size(),8)

        g.remove_node(3)
        self.assertEqual(g.v_size(), 7)



    def test_remove_edge(self):
        g = self.creat_g()

        g.remove_edge(5,1)

        self.assertTrue(g.e_size(),9)
