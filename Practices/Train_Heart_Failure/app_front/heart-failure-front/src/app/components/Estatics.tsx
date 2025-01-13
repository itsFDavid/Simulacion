"use client";
import Image from "next/image";

export default function Statics() {
  return (
    <div className="w-full bg-black">
      <div className="grid grid-cols-3">
        <div>
          <Image
            src="/curva_pr.png"
            alt="Imagen de curva de precision"
            width={400}
            height={300}
            className="py-10 px-3"
          />
          Curva de precision
        </div>

        <div>
          <Image
            src="/curva_roc.png"
            alt="Imagen de curva ROC"
            width={400}
            height={300}
            className="py-10 px-3"
          />
          Curva ROC
        </div>

        <div>
          <Image
            src="/matriz_corr_test_set.png"
            alt="Imagen de matriz de correlacion de test set"
            width={400}
            height={300}
            className="py-10 px-3"
          />
          Matriz de correlacion con test set
        </div>

        <div>
          <Image
            src="/matriz_corr_val_set.png"
            alt="Imagen de matriz de correlacion de val set"
            width={400}
            height={300}
            className="py-10 px-3"
          />
          Matriz de correlacion con val set
        </div>
      </div>
    </div>
  );
}