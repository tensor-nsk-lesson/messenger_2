PGDMP                            w            messenger_2 #   10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)    11.3 5    }           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            ~           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �           1262    16880    messenger_2    DATABASE     }   CREATE DATABASE messenger_2 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'ru_RU.UTF-8' LC_CTYPE = 'ru_RU.UTF-8';
    DROP DATABASE messenger_2;
             postgres    false            �           0    0    DATABASE messenger_2    ACL     2   GRANT ALL ON DATABASE messenger_2 TO messenger_2;
                  postgres    false    2944            �            1259    16897    Authorization    TABLE     �   CREATE TABLE public."Authorization" (
    id_auth integer NOT NULL,
    id_user integer,
    user_number integer,
    password integer
);
 #   DROP TABLE public."Authorization";
       public         messenger_2    false            �            1259    16895    Authorization_id_auth_seq    SEQUENCE     �   CREATE SEQUENCE public."Authorization_id_auth_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public."Authorization_id_auth_seq";
       public       messenger_2    false    197            �           0    0    Authorization_id_auth_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."Authorization_id_auth_seq" OWNED BY public."Authorization".id_auth;
            public       messenger_2    false    196            �            1259    16918    Chat    TABLE     m   CREATE TABLE public."Chat" (
    id_chat integer NOT NULL,
    id_user integer,
    id_permission integer
);
    DROP TABLE public."Chat";
       public         messenger_2    false            �            1259    16916    Chat_id_chat_seq    SEQUENCE     �   CREATE SEQUENCE public."Chat_id_chat_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."Chat_id_chat_seq";
       public       messenger_2    false    201            �           0    0    Chat_id_chat_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public."Chat_id_chat_seq" OWNED BY public."Chat".id_chat;
            public       messenger_2    false    200            �            1259    16937    Content    TABLE     f   CREATE TABLE public."Content" (
    id_message integer,
    text_message text,
    id_user integer
);
    DROP TABLE public."Content";
       public         messenger_2    false            �            1259    16931    Message    TABLE     �   CREATE TABLE public."Message" (
    id_message integer NOT NULL,
    id_chat integer,
    id_user integer,
    "time" timestamp without time zone
);
    DROP TABLE public."Message";
       public         messenger_2    false            �            1259    16929    Message_id_message_seq    SEQUENCE     �   CREATE SEQUENCE public."Message_id_message_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public."Message_id_message_seq";
       public       messenger_2    false    204            �           0    0    Message_id_message_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public."Message_id_message_seq" OWNED BY public."Message".id_message;
            public       messenger_2    false    203            �            1259    16924 
   Permission    TABLE     c   CREATE TABLE public."Permission" (
    id_permission integer NOT NULL,
    type_permission text
);
     DROP TABLE public."Permission";
       public         messenger_2    false            �            1259    16907    User    TABLE     �   CREATE TABLE public."User" (
    id_user integer NOT NULL,
    age integer,
    user_name text,
    avatar text,
    status text,
    visit_time timestamp without time zone
);
    DROP TABLE public."User";
       public         messenger_2    false            �            1259    16905    User_id_user_seq    SEQUENCE     �   CREATE SEQUENCE public."User_id_user_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."User_id_user_seq";
       public       messenger_2    false    199            �           0    0    User_id_user_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public."User_id_user_seq" OWNED BY public."User".id_user;
            public       messenger_2    false    198            �
           2604    16900    Authorization id_auth    DEFAULT     �   ALTER TABLE ONLY public."Authorization" ALTER COLUMN id_auth SET DEFAULT nextval('public."Authorization_id_auth_seq"'::regclass);
 F   ALTER TABLE public."Authorization" ALTER COLUMN id_auth DROP DEFAULT;
       public       messenger_2    false    197    196    197            �
           2604    16921    Chat id_chat    DEFAULT     p   ALTER TABLE ONLY public."Chat" ALTER COLUMN id_chat SET DEFAULT nextval('public."Chat_id_chat_seq"'::regclass);
 =   ALTER TABLE public."Chat" ALTER COLUMN id_chat DROP DEFAULT;
       public       messenger_2    false    200    201    201            �
           2604    16934    Message id_message    DEFAULT     |   ALTER TABLE ONLY public."Message" ALTER COLUMN id_message SET DEFAULT nextval('public."Message_id_message_seq"'::regclass);
 C   ALTER TABLE public."Message" ALTER COLUMN id_message DROP DEFAULT;
       public       messenger_2    false    203    204    204            �
           2604    16910    User id_user    DEFAULT     p   ALTER TABLE ONLY public."User" ALTER COLUMN id_user SET DEFAULT nextval('public."User_id_user_seq"'::regclass);
 =   ALTER TABLE public."User" ALTER COLUMN id_user DROP DEFAULT;
       public       messenger_2    false    199    198    199            r          0    16897    Authorization 
   TABLE DATA               R   COPY public."Authorization" (id_auth, id_user, user_number, password) FROM stdin;
    public       messenger_2    false    197   :       v          0    16918    Chat 
   TABLE DATA               A   COPY public."Chat" (id_chat, id_user, id_permission) FROM stdin;
    public       messenger_2    false    201   6:       z          0    16937    Content 
   TABLE DATA               F   COPY public."Content" (id_message, text_message, id_user) FROM stdin;
    public       messenger_2    false    205   S:       y          0    16931    Message 
   TABLE DATA               I   COPY public."Message" (id_message, id_chat, id_user, "time") FROM stdin;
    public       messenger_2    false    204   p:       w          0    16924 
   Permission 
   TABLE DATA               F   COPY public."Permission" (id_permission, type_permission) FROM stdin;
    public       messenger_2    false    202   �:       t          0    16907    User 
   TABLE DATA               U   COPY public."User" (id_user, age, user_name, avatar, status, visit_time) FROM stdin;
    public       messenger_2    false    199   �:       �           0    0    Authorization_id_auth_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."Authorization_id_auth_seq"', 1, false);
            public       messenger_2    false    196            �           0    0    Chat_id_chat_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Chat_id_chat_seq"', 1, false);
            public       messenger_2    false    200            �           0    0    Message_id_message_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."Message_id_message_seq"', 1, false);
            public       messenger_2    false    203            �           0    0    User_id_user_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."User_id_user_seq"', 1, false);
            public       messenger_2    false    198            �
           2606    16902     Authorization Authorization_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public."Authorization"
    ADD CONSTRAINT "Authorization_pkey" PRIMARY KEY (id_auth);
 N   ALTER TABLE ONLY public."Authorization" DROP CONSTRAINT "Authorization_pkey";
       public         messenger_2    false    197            �
           2606    16923    Chat Chat_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."Chat"
    ADD CONSTRAINT "Chat_pkey" PRIMARY KEY (id_chat);
 <   ALTER TABLE ONLY public."Chat" DROP CONSTRAINT "Chat_pkey";
       public         messenger_2    false    201            �
           2606    16936    Message Message_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT "Message_pkey" PRIMARY KEY (id_message);
 B   ALTER TABLE ONLY public."Message" DROP CONSTRAINT "Message_pkey";
       public         messenger_2    false    204            �
           2606    16928    Permission Permission_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public."Permission"
    ADD CONSTRAINT "Permission_pkey" PRIMARY KEY (id_permission);
 H   ALTER TABLE ONLY public."Permission" DROP CONSTRAINT "Permission_pkey";
       public         messenger_2    false    202            �
           2606    16915    User User_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id_user);
 <   ALTER TABLE ONLY public."User" DROP CONSTRAINT "User_pkey";
       public         messenger_2    false    199            �
           1259    16948    fki_Authorization_fkey    INDEX     W   CREATE INDEX "fki_Authorization_fkey" ON public."Authorization" USING btree (id_user);
 ,   DROP INDEX public."fki_Authorization_fkey";
       public         messenger_2    false    197            �
           1259    16960    fki_Chat_permission_fkey    INDEX     V   CREATE INDEX "fki_Chat_permission_fkey" ON public."Chat" USING btree (id_permission);
 .   DROP INDEX public."fki_Chat_permission_fkey";
       public         messenger_2    false    201            �
           1259    16954    fki_Chat_user_fkey    INDEX     J   CREATE INDEX "fki_Chat_user_fkey" ON public."Chat" USING btree (id_user);
 (   DROP INDEX public."fki_Chat_user_fkey";
       public         messenger_2    false    201            �
           1259    16966    fki_Content_fkey    INDEX     N   CREATE INDEX "fki_Content_fkey" ON public."Content" USING btree (id_message);
 &   DROP INDEX public."fki_Content_fkey";
       public         messenger_2    false    205            �
           1259    17739    fki_Content_user_fkey    INDEX     P   CREATE INDEX "fki_Content_user_fkey" ON public."Content" USING btree (id_user);
 +   DROP INDEX public."fki_Content_user_fkey";
       public         messenger_2    false    205            �
           1259    16972    fki_Message_chat_fkey    INDEX     P   CREATE INDEX "fki_Message_chat_fkey" ON public."Message" USING btree (id_chat);
 +   DROP INDEX public."fki_Message_chat_fkey";
       public         messenger_2    false    204            �
           1259    16978    fki_me    INDEX     ?   CREATE INDEX fki_me ON public."Message" USING btree (id_user);
    DROP INDEX public.fki_me;
       public         messenger_2    false    204            �
           2606    16943     Authorization Authorization_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Authorization"
    ADD CONSTRAINT "Authorization_fkey" FOREIGN KEY (id_user) REFERENCES public."User"(id_user);
 N   ALTER TABLE ONLY public."Authorization" DROP CONSTRAINT "Authorization_fkey";
       public       messenger_2    false    197    2788    199            �
           2606    16955    Chat Chat_permission_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Chat"
    ADD CONSTRAINT "Chat_permission_fkey" FOREIGN KEY (id_permission) REFERENCES public."Permission"(id_permission);
 G   ALTER TABLE ONLY public."Chat" DROP CONSTRAINT "Chat_permission_fkey";
       public       messenger_2    false    201    2794    202            �
           2606    16949    Chat Chat_user_fkey    FK CONSTRAINT     |   ALTER TABLE ONLY public."Chat"
    ADD CONSTRAINT "Chat_user_fkey" FOREIGN KEY (id_user) REFERENCES public."User"(id_user);
 A   ALTER TABLE ONLY public."Chat" DROP CONSTRAINT "Chat_user_fkey";
       public       messenger_2    false    201    199    2788            �
           2606    16961    Content Content_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Content"
    ADD CONSTRAINT "Content_fkey" FOREIGN KEY (id_message) REFERENCES public."Message"(id_message);
 B   ALTER TABLE ONLY public."Content" DROP CONSTRAINT "Content_fkey";
       public       messenger_2    false    2796    205    204            �
           2606    17734    Content Content_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Content"
    ADD CONSTRAINT "Content_user_fkey" FOREIGN KEY (id_user) REFERENCES public."User"(id_user);
 G   ALTER TABLE ONLY public."Content" DROP CONSTRAINT "Content_user_fkey";
       public       messenger_2    false    199    205    2788            �
           2606    16967    Message Message_chat_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT "Message_chat_fkey" FOREIGN KEY (id_chat) REFERENCES public."Chat"(id_chat);
 G   ALTER TABLE ONLY public."Message" DROP CONSTRAINT "Message_chat_fkey";
       public       messenger_2    false    204    2790    201            �
           2606    16973    Message Message_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Message"
    ADD CONSTRAINT "Message_user_fkey" FOREIGN KEY (id_user) REFERENCES public."User"(id_user);
 G   ALTER TABLE ONLY public."Message" DROP CONSTRAINT "Message_user_fkey";
       public       messenger_2    false    2788    199    204            �           826    16882    DEFAULT PRIVILEGES FOR TABLES    DEFAULT ACL     P   ALTER DEFAULT PRIVILEGES FOR ROLE postgres GRANT ALL ON TABLES  TO messenger_2;
                  postgres    false            r      x������ � �      v      x������ � �      z      x������ � �      y      x������ � �      w      x������ � �      t      x������ � �     